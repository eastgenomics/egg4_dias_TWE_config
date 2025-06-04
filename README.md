# egg4_dias_TWE_config

This repo contains a JSON config file which is used with eggd_dias_batch to specify inputs for running the Dias pipeline for TWE data.

## What does the config do?
eggd_dias_batch ([https://github.com/eastgenomics/eggd_dias_batch](https://github.com/eastgenomics/eggd_dias_batch)) is a DNAnexus app that runs the Dias pipeline for germline sequence data analysis. The egg4_dias_TWE_config repo contains the dias_TWE_config file that specifies the executables and their input files to be used in the Dias pipeline for analysing TWE data.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself.

## Parts of the config
The config specifies app IDs and workflow IDs at the top, followed by a `reference_files` dict for inputs that could be used in multiple running modes. The `modes` section specifies inputs specific to a running mode:
* cnv_call
    * specifies inputs for CNV calling.
* snv_reports
    * specifies the inputs for snv_reports.
* artemis
    * specifies inputs for [eggd_artemis](https://github.com/eastgenomics/eggd_artemis).

## Versions of workflows, apps, and dynamic files in the config
| Type | Name | dias_TWE_config_GRCh37_v3.3.1.json | dias_TWE_config_GRCh38_v4.0.0.json |
| -- | -- | -- | -- |
| App | **eggd_artemis** | v1.5.0 (`app-GkbJ7p0463bjk9VKv3x8G5F8`) | v1.6.0 (`app-GxVK0bQ4KzQzXkJ3Xg53ypXv`) |
| App | **eggd_GATKgCNV_call** | - | v2.0.0 (`app-GvZB5p846Vg69fBg0Fq10938`)
| Workflow | **dias_reports** | dias_reports_v2.2.2 (`workflow-GkbJY284FpfgqF8ggz57fVY2`) | dias_reports_v2.2.2 (`workflow-GkbJY284FpfgqF8ggz57fVY2`) |
| File | **genepanels** | 241024_genepanels.tsv (`file-GvJ5fbQ4qQYq73gjGyP57zFB`) | 250528_genepanels.tsv (`file-J0qJKv04Kp44F8JB3004390k`) |
| File | **panel_dump for eggd_optimised_filtering** | 241030_panelapp_dump.json (`file-GvVg3qj4Y54jBF8bgX62gkfQ`) | 250530_panelapp_dump.json (`file-J0yk3V04VVYxJ9bz3QPPzxPg`) |
| File | **exons** | GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv (`file-GF611Z8433Gk7gZ47gypK7ZZ`) | GCF_000001405.39_GRCh38.p13_genomic_20211119.exon_5bp.tsv (`file-GyFfgpQ4fJPv132574bFQfV5`) |
| File | **genes2transcripts** | 240402_g2t.tsv (`file-Gj770X8433Gb506pjq1PxXG9`) | g2t_grch38_v2.0.0.tsv (`file-J0v6GyQ4zqZJV047q56PqFx5`) |
| File | **exons_with_symbols for eggd_athena** | GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv (`file-GF611Z8433Gf99pBPbJkV7bq`) | GCF_000001405.39_GRCh38.p13_genomic_20211119.symbols.exon_5bp.tsv (`file-Gyb29P84fJPqZJ37pfjz1vZB`) |
| File | **twe_vep_config for SNV reports** | twe_vep_config_v1.2.1.json (`file-J051vX04j4fjv5YvY53JJK3V`) | twe_vep_config_GRCh38_v1.1.1.json(`file-J0gKQ604j4fvJQvk92Z5KqGV`) |
