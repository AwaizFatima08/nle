import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:nle_prep/ads/ad_service.dart';
import 'package:nle_prep/app.dart';
import 'package:nle_prep/content/content_repository.dart';
import 'package:nle_prep/core/scoring.dart';
import 'package:nle_prep/features/exam/exam_notifier.dart';
import 'package:nle_prep/ui/async_value_view.dart';
import 'package:nle_prep/ui/theme.dart';

class ResultsScreen extends ConsumerStatefulWidget {
  const ResultsScreen({required this.attemptId, super.key});

  final String attemptId;

  @override
  ConsumerState<ResultsScreen> createState() => _ResultsScreenState();
}

class _ResultsScreenState extends ConsumerState<ResultsScreen> {
  Future<void> _home() async {
    await ref.read(adServiceProvider).showReportInterstitial();
    if (mounted) context.go('/');
  }

  @override
  Widget build(BuildContext context) {
    final l10n = context.l10n;
    return AsyncValueView(
      value: ref.watch(reviewProvider(widget.attemptId)),
      data: (exam) {
        final score = scoreSitting(exam.sitting, exam.attempt.answers);
        return Scaffold(
          appBar: AppBar(title: Text(exam.sitting.paper.title)),
          body: ListView(
            padding: const EdgeInsetsDirectional.all(AppSpacing.md),
            children: [
              _ScoreCard(score: score),
              const SizedBox(height: AppSpacing.md),
              FilledButton.icon(
                onPressed: () => unawaited(context.push('/review/${widget.attemptId}')),
                icon: const Icon(Icons.menu_book_outlined),
                label: Text(l10n.reviewAnswers),
              ),
              const SizedBox(height: AppSpacing.lg),
              Text(l10n.byGroup, style: Theme.of(context).textTheme.titleMedium),
              _GroupScores(score: score),
              const SizedBox(height: AppSpacing.lg),
              Text(
                l10n.bySection,
                style: Theme.of(context).textTheme.titleMedium,
              ),
              for (final section in score.sections) _ScoreRow(section.title, section.tally),
              const SizedBox(height: AppSpacing.lg),
              Text(
                l10n.weakTopics,
                style: Theme.of(context).textTheme.titleMedium,
              ),
              _WeakTopics(score: score),
              const SizedBox(height: AppSpacing.md),
              OutlinedButton(
                onPressed: () => unawaited(_home()),
                child: Text(l10n.backHome),
              ),
            ],
          ),
        );
      },
    );
  }
}

class _ScoreCard extends StatelessWidget {
  const _ScoreCard({required this.score});

  final TestScore score;

  @override
  Widget build(BuildContext context) {
    final l10n = context.l10n;
    final overall = score.overall;
    final passed = overall.percent >= passPercent;
    return Card(
      child: Padding(
        padding: const EdgeInsetsDirectional.all(AppSpacing.lg),
        child: Column(
          children: [
            Text(l10n.results, style: Theme.of(context).textTheme.titleMedium),
            Text(
              l10n.percentLabel(overall.percent),
              style: Theme.of(context).textTheme.displayMedium,
            ),
            Text(l10n.scoreOutOf(overall.correct, overall.total)),
            const SizedBox(height: AppSpacing.sm),
            Chip(
              avatar: Icon(passed ? Icons.check_circle_outline : Icons.trending_up),
              label: Text(passed ? l10n.passAbove : l10n.passBelow),
            ),
            Text(l10n.passLine, style: Theme.of(context).textTheme.bodySmall),
            const SizedBox(height: AppSpacing.sm),
            Text(
              l10n.scoreNote(overall.total - score.skipped, score.skipped),
              textAlign: TextAlign.center,
              style: Theme.of(context).textTheme.bodySmall,
            ),
          ],
        ),
      ),
    );
  }
}

/// PM&DC's minimum pass percentage for the NRE theory component.
const passPercent = 60;

/// Clinical (140) and applied basic sciences (60) halves of the paper.
class _GroupScores extends ConsumerWidget {
  const _GroupScores({required this.score});

  final TestScore score;

  @override
  Widget build(BuildContext context, WidgetRef ref) => AsyncBody(
    value: ref.watch(catalogProvider),
    data: (catalog) {
      var clinical = const Tally(0, 0);
      var basic = const Tally(0, 0);
      for (final topic in score.topics) {
        final t = topic.tally;
        if (catalog.isBasic(topic.section)) {
          basic = Tally(basic.correct + t.correct, basic.total + t.total);
        } else {
          clinical = Tally(clinical.correct + t.correct, clinical.total + t.total);
        }
      }
      return Column(
        children: [
          _ScoreRow(context.l10n.groupClinical, clinical),
          _ScoreRow(context.l10n.groupBasic, basic),
        ],
      );
    },
  );
}

class _ScoreRow extends StatelessWidget {
  const _ScoreRow(this.title, this.tally);

  final String title;
  final Tally tally;

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsetsDirectional.only(top: AppSpacing.sm),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Flexible(child: Text(title)),
            Text(context.l10n.scoreOutOf(tally.correct, tally.total)),
          ],
        ),
        const SizedBox(height: AppSpacing.xs),
        LinearProgressIndicator(value: tally.percent / 100),
      ],
    ),
  );
}

class _WeakTopics extends ConsumerWidget {
  const _WeakTopics({required this.score});

  final TestScore score;

  static const _shown = 5;

  @override
  Widget build(BuildContext context, WidgetRef ref) => AsyncBody(
    value: ref.watch(catalogProvider),
    data: (catalog) => Column(
      children: [
        for (final topic in score.topics.take(_shown))
          _ScoreRow(
            catalog.topicTitle(topic.section, topic.topic),
            topic.tally,
          ),
      ],
    ),
  );
}
