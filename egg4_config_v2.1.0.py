assay_name = "TWE" # Twist Whole Exome
assay_version = "v2.1.0"

ref_project_id = "project-Fkb6Gkj433GVVvj73J7x8KbV"

### Dynamic files:

## for generate_bed
# genepanels 230602
genepanels_file = "{}:file-GVx0vkQ433Gvq63k1Kj4Y562".format(ref_project_id)
# g2t 230421
genes2transcripts = "{}:file-GV4P970433Gj6812zGVBZvB4".format(ref_project_id)
# GCF_000001405.25_GRCh37.p13_genomic.exon_5bp_v2.0.0.tsv
exons_nirvana = "{}:file-GF611Z8433Gk7gZ47gypK7ZZ".format(ref_project_id)

# for generate_bed_for_VEP
vep_bed_flank = 495

## for eggd_Athena
# GCF_000001405.25_GRCh37.p13_genomic.symbols.exon_5bp_v2.0.0.tsv
exons_file = "{}:file-GF611Z8433Gf99pBPbJkV7bq".format(ref_project_id)

## for eggd_VEP
# VEP config file for SNV reports v1.1.6
vep_config = "{}:file-GYX8q204j4fpP18Qx7YGkJvX".format(ref_project_id)


### Apps and workflows:

# dias_reports
# v2.1.0
rpt_workflow_id = "{}:workflow-GXzkfYj4QPQp9z4Jz4BF09y6".format(ref_project_id)

generate_bed_vep_stage_id = "stage-rpt_generate_bed_vep"
vep_stage_id = "stage-rpt_vep"
generate_workbook_stage_id = "stage-rpt_generate_workbook"
generate_bed_athena_stage_id = "stage-rpt_generate_bed_athena"
athena_stage_id = "stage-rpt_athena"

rpt_dynamic_files = {
    # inputs for generate bed for vep
    "{}.exons_nirvana ID".format(generate_bed_vep_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_vep_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_vep_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_vep_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_vep_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_vep_stage_id): "",
    # inputs for eggd_vep
    "{}.config_file ID".format(vep_stage_id): vep_config,
    "{}.config_file".format(vep_stage_id): "",
    # inputs for generate_variant_workbook
    "{}.exclude_columns".format(generate_workbook_stage_id): "BaseQRankSum ClippingRankSum DB ExcessHet FS MLEAC MLEAF MQ MQRankSum QD ReadPosRankSum SOR PL QUAL ID FILTER  CSQ_ClinVar_CLNSIGCONF  CSQ_Allele CSQ_HGNC_ID DP AC AF AN CSQ_SpliceAI_pred_DP_AL CSQ_SpliceAI_pred_DP_AG CSQ_SpliceAI_pred_DP_DG CSQ_SpliceAI_pred_DP_DL",
    "{}.acmg".format(generate_workbook_stage_id): "true",
    "{}.rename_columns".format(generate_workbook_stage_id): "CSQ_Feature=Transcript DP_FMT=DP",
    "{}.add_comment_column".format(generate_workbook_stage_id): "true",
    "{}.keep_tmp".format(generate_workbook_stage_id): "true",
    "{}.summary".format(generate_workbook_stage_id): "dias",
    "{}.filter".format(generate_workbook_stage_id): "bcftools filter -e '(CSQ_Consequence==\"synonymous_variant\" | CSQ_Consequence==\"intron_variant\" | CSQ_Consequence==\"upstream_gene_variant\" | CSQ_Consequence==\"downstream_gene_variant\" | CSQ_Consequence==\"intergenic_variant\" | CSQ_Consequence==\"5_prime_UTR_variant\" | CSQ_Consequence==\"3_prime_UTR_variant\" | CSQ_gnomADe_AF>0.01 | CSQ_gnomADg_AF>0.01 | CSQ_TWE_AF>0.05) & CSQ_HGMD_CLASS!~ \"DM\" & CSQ_ClinVar_CLNSIG!~ \"pathogenic\\/i\" & CSQ_ClinVar_CLNSIGCONF!~ \"pathogenic\\/i\"'",
    "{}.human_filter".format(generate_workbook_stage_id): "excluded gnomAD exomes / genomes > 1%, TWE > 5%, synonymous / intronic / intergenic / upstream / downstream / UTRs EXCEPT pathogenic status in ClinVar OR DM in HGMD Class",
    "{}.reorder_columns".format(generate_workbook_stage_id): "CHROM POS REF ALT GT GQ DP_FMT AD CSQ_SYMBOL CSQ_EXON CSQ_INTRON CSQ_HGVSc CSQ_HGVSp CSQ_Consequence CSQ_IMPACT CSQ_VARIANT_CLASS CSQ_gnomADe_AF CSQ_gnomADe_Hom CSQ_gnomADe_AC CSQ_gnomADe_AN CSQ_gnomADg_AF CSQ_gnomADg_AC CSQ_gnomADg_AN CSQ_TWE_AF CSQ_TWE_AC_Hom CSQ_TWE_AC_Het CSQ_TWE_AN CSQ_HGMD CSQ_HGMD_CLASS CSQ_HGMD_RANKSCORE CSQ_HGMD_PHEN CSQ_Existing_variation CSQ_ClinVar CSQ_ClinVar_CLNDN CSQ_ClinVar_CLNSIG CSQ_Mastermind_MMID3 CSQ_CADD_PHRED CSQ_REVEL CSQ_SpliceAI_pred_DS_AG CSQ_SpliceAI_pred_DS_AL CSQ_SpliceAI_pred_DS_DG CSQ_SpliceAI_pred_DS_DL CSQ_HGVS_OFFSET CSQ_STRAND CSQ_Feature",
    # inputs for generate bed for athena
    "{}.exons_nirvana ID".format(generate_bed_athena_stage_id): exons_nirvana,
    "{}.exons_nirvana".format(generate_bed_athena_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_athena_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_athena_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_athena_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_athena_stage_id): "",
    # inputs for athena
    "{}.exons_file ID".format(athena_stage_id): exons_file,
    "{}.exons_file".format(athena_stage_id): "",
    "{}.limit".format(athena_stage_id): "260",
    "{}.summary".format(athena_stage_id): "true"
}

# Sample-specific input files and their search patterns
rpt_stage_input_dict = {
    # eggd_vep
    "{}.vcf".format(vep_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    # eggd_athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}

