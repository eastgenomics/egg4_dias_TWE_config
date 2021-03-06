import sys

sys.path.append("/mnt/storage/apps/software/dias_config/")

from dias_dynamic_files import (
    genes2transcripts,
    bioinformatic_manifest,
    genepanels_file,
)

assay_name = "TWE" # Twist Whole Exome
assay_version = "v1.1.6"

ref_project_id = "project-Fkb6Gkj433GVVvj73J7x8KbV"

# Single workflow

ss_workflow_id = "{}:workflow-G5gzKx8433GYp8x7FkjV1J2j".format(ref_project_id)

sentieon_stage_id = "stage-Fy6fpk040vZZPPbq96Jb2KfK"

sentieon_R1_input_stage = "{}.reads_fastqgzs".format(sentieon_stage_id)
sentieon_R2_input_stage = "{}.reads2_fastqgzs".format(sentieon_stage_id)
sentieon_sample_input_stage = "{}.sample".format(sentieon_stage_id)
fastqc_fastqs_input_stage = "stage-Fy6fpV840vZZ0v6J8qBQYqZF.fastqs"
ss_beds_inputs = {
    # vcf_qc
    "stage-Fy6fqy040vZV3Gj24vppvJgZ.bed_file ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-Fy6fqy040vZV3Gj24vppvJgZ.bed_file": "",
    # region coverage
    "stage-G21GzGj433Gky42j42Q5bJkf.input_bed ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-G21GzGj433Gky42j42Q5bJkf.input_bed": "",
    # mosdepth
    "stage-Fy6fvYQ40vZV1y8p9GYKPYyQ.bed ID": "file-Fpz2X0Q433GVK5xxPvzqvVPB",
    "stage-Fy6fvYQ40vZV1y8p9GYKPYyQ.bed": "",
    # picard
    "stage-Fy6fx2Q40vZbFVxZ283xXGVY.bedfile ID": "file-G2J5ZV0433GQJz7860vb4PB1",  # Twist Capture Bed
    "stage-Fy6fx2Q40vZbFVxZ283xXGVY.bedfile": ""
}


# Multi workflow

happy_stage_id = "stage-Fq1BPKj433Gx3K4Y8J35j0fv"

happy_stage_prefix = "{}.prefix".format(happy_stage_id)
happy_stage_bed = {
    "{}.panel_bed ID".format(happy_stage_id): "file-G2V8k90433GVQ7v07gfj0ggX",
    "{}.panel_bed".format(happy_stage_id): "file-G2V8k90433GVQ7v07gfj0ggX"
}

female_threshold = 60
male_threshold = 1

somalier_relate_stage_id = "stage-G5j1jJj433GpFY3v0JZQ2ZZ0"

multi_stage_input_dict = {
    "stage-Fybykxj433GV7vJKFGf3yVkK.SampleSheet": {
        "app": None, "subdir": "", "pattern": "SampleSheet.csv$",
    },
    "{}.query_vcf".format(happy_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "^NA12878-.*-EGG4_markdup_recalibrated_Haplotyper.vcf.gz$",
    },
    "{}.somalier_extract_file".format(somalier_relate_stage_id): {
        "app": "somalier_extract", "subdir": "",
        "pattern": "-E '(.*).somalier$'"
    },
}

ms_workflow_id = "{}:workflow-G5j1j28433GYkv4gPpPG8g11".format(ref_project_id)

# MultiQC

mqc_applet_id = "app-G6FyybQ4f4xqqpFfGqg34y2Y"
mqc_config_file = "{}:file-G82Y3Kj433GV6bG91pB5VzG0".format(ref_project_id)

# Reports

xlsx_flanks = 495

cds_file = "{}:file-GF611Z8433Gk7gZ47gypK7ZZ".format(ref_project_id)
cds_file_for_athena = "{}:file-GF611Z8433Gf99pBPbJkV7bq".format(ref_project_id)
vep_config = "{}:file-GB69B1j43Vx9f0ZYGbKf9xQ1".format(ref_project_id)

generate_bed_vep_stage_id = "stage-G9P8p104vyJJGy6y86FQBxkv"
vep_stage_id = "stage-G9Q0jzQ4vyJ3x37X4KBKXZ5v"
generate_workbook_stage_id = "stage-G9P8VQj4vyJBJ0kg50vzVPxY"
generate_bed_athena_stage_id = "stage-Fyq5yy0433GXxz691bKyvjPJ"
athena_stage_id = "stage-Fyq5z18433GfYZbp3vX1KqjB"

rpt_workflow_id = "{}:workflow-GBQ985Q433GYJjv0379PJqqg".format(ref_project_id)

rpt_stage_input_dict = {
    # generate_bed
    "{}.sample_file".format(generate_bed_athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        "pattern": "-E '{}(.*).per-base.bed.gz.csi$'"
    },
    "{}.sample_file".format(generate_bed_vep_stage_id): {
        "app": "mosdepth", "subdir": "",
        "pattern": "-E '{}(.*).per-base.bed.gz.csi$'"
    },
    # vep
    "{}.vcf".format(vep_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    # athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}

rpt_dynamic_files = {
    # inputs for generate bed for vep
    "{}.exons_nirvana ID".format(generate_bed_vep_stage_id): cds_file,
    "{}.exons_nirvana".format(generate_bed_vep_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_vep_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_vep_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_vep_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_vep_stage_id): "",
    "{}.manifest ID".format(generate_bed_vep_stage_id): bioinformatic_manifest,
    "{}.manifest".format(generate_bed_vep_stage_id): "",
    # inputs for generate bed for athena
    "{}.exons_nirvana ID".format(generate_bed_athena_stage_id): cds_file,
    "{}.exons_nirvana".format(generate_bed_athena_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_athena_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_athena_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_athena_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_athena_stage_id): "",
    "{}.manifest ID".format(generate_bed_athena_stage_id): bioinformatic_manifest,
    "{}.manifest".format(generate_bed_athena_stage_id): "",
    # inputs for athena
    "{}.exons_file ID".format(athena_stage_id): cds_file_for_athena,
    "{}.exons_file".format(athena_stage_id): ""
}

# reanalysis

rea_stage_input_dict = {
    # vep
    "{}.vcf".format(vep_stage_id): {
        "app": "sentieon-dnaseq", "subdir": "",
        "pattern": "-E '{}(.*)[^g].vcf.gz$'"
    },
    # athena
    "{}.mosdepth_files".format(athena_stage_id): {
        "app": "mosdepth", "subdir": "",
        # athena requires both per-base files and reference files
        "pattern": "-E '{}(.*)(per-base.bed.gz$|reference)'"
    },
}

rea_dynamic_files = {
    # inputs for generate bed for vep
    "{}.exons_nirvana ID".format(generate_bed_vep_stage_id): cds_file,
    "{}.exons_nirvana".format(generate_bed_vep_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_vep_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_vep_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_vep_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_vep_stage_id): "",
    # inputs for generate bed for athena
    "{}.exons_nirvana ID".format(generate_bed_athena_stage_id): cds_file,
    "{}.exons_nirvana".format(generate_bed_athena_stage_id): "",
    "{}.nirvana_genes2transcripts ID".format(generate_bed_athena_stage_id): genes2transcripts,
    "{}.nirvana_genes2transcripts".format(generate_bed_athena_stage_id): "",
    "{}.gene_panels ID".format(generate_bed_athena_stage_id): genepanels_file,
    "{}.gene_panels".format(generate_bed_athena_stage_id): "",
    # inputs for athena
    "{}.exons_file ID".format(athena_stage_id): cds_file_for_athena,
    "{}.exons_file".format(athena_stage_id): ""
}
