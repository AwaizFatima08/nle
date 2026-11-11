import 'dart:async';

import 'package:flutter/material.dart';
import 'package:nle_prep/app.dart';
import 'package:nle_prep/ui/theme.dart';
import 'package:url_launcher/url_launcher.dart';

/// PM&DC pages the exam information in this app comes from (Play Misleading
/// Claims policy: government information needs its official source).
abstract final class OfficialSources {
  static const pmdc = 'https://pmdc.pk';
  static const syllabus = 'https://pmdc.pk/Publication/Syllabus';
  static const portal = 'https://nre.pmdc.pk';
}

/// The "not a government app" notice, with links to PM&DC when [showLinks].
class OfficialSourcesCard extends StatelessWidget {
  const OfficialSourcesCard({this.showLinks = true, super.key});

  final bool showLinks;

  void _open(String url) => unawaited(
    launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication),
  );

  @override
  Widget build(BuildContext context) {
    final l10n = context.l10n;
    final theme = Theme.of(context);
    return Card(
      color: theme.colorScheme.secondaryContainer,
      child: Padding(
        padding: const EdgeInsetsDirectional.symmetric(vertical: AppSpacing.sm),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsetsDirectional.symmetric(horizontal: AppSpacing.md),
              child: Text(l10n.notGovernment, style: theme.textTheme.bodyMedium),
            ),
            if (showLinks) ...[
              const SizedBox(height: AppSpacing.xs),
              _SourceLink(l10n.sourcePmdc, OfficialSources.pmdc, _open),
              _SourceLink(l10n.sourceSyllabus, OfficialSources.syllabus, _open),
              _SourceLink(l10n.sourcePortal, OfficialSources.portal, _open),
            ],
          ],
        ),
      ),
    );
  }
}

class _SourceLink extends StatelessWidget {
  const _SourceLink(this.label, this.url, this.onOpen);

  final String label;
  final String url;
  final void Function(String url) onOpen;

  @override
  Widget build(BuildContext context) => ListTile(
    dense: true,
    leading: const Icon(Icons.open_in_new),
    title: Text(label),
    subtitle: Text(url),
    onTap: () => onOpen(url),
  );
}
