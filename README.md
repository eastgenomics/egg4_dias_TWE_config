# dias_TWE_config_GRCh37_v3.1.0.json

This repo contains a JSON config file which is used with eggd_dias_batch to specify inputs for running the Dias pipeline for TWE data.

## What does the config do?
eggd_dias_batch ([https://github.com/eastgenomics/dias_batch_running](https://github.com/eastgenomics/dias_batch_running)) is a DNAnexus app that runs the Dias pipeline for germline sequence data analysis. The egg4_dias_TWE_config repo contains the dias_TWE_config file that specifies the executables and their input files to be used in the Dias pipeline for analysing TWE data on build GRCh37.

New versions of apps and app inputs for use in the Dias pipeline can be updated in the config without needing to update the pipeline itself.

## Parts of the config
The config specifies app IDs and workflow IDs at the top, followed by a `reference_files` dict for inputs that could be used in multiple running modes. The `modes` section specifies inputs specific to a running mode. The TWE config currently only has one running mode:
* dias_reports
    * specifies the  inputs for dias_reports.

## Versions of workflows and dynamic files in the config
Workflows:
* Dias reports: **dias_reports_v2.1.0**
    * DNAnexus workflow ID: `workflow-GXzkfYj4QPQp9z4Jz4BF09y6`

Dynamic files:
| File      | File name | DNAnexus file ID |
| --------- | --------- | ---------------- |
| genepanels | **230602_genepanels.tsv** | `file-GVx0vkQ433Gvq63k1Kj4Y562` |
| exons_nirvana | **GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gk7gZ47gypK7ZZ` |
| genes2transcripts | **230421_g2t.tsv** | `file-GV4P970433Gj6812zGVBZvB4` |
| exons_file for eggd_athena | **GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv** | `file-GF611Z8433Gf99pBPbJkV7bq` |
| twe_vep_config for SNV reports | **twe_vep_config_v1.1.12.json** | `file-GfZP8884j4fzp14Y3gPZVZF1` |
