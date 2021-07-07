

# run_model.R --input /input/directory --output /output/directory
# model.py --input /input/directory --output /output/directory

# All input files should be mounted in a directory called /input in the working directory of the container.

# library(readr)
# library(plyr)
# library(optparse)

# option_list = list(
#   make_option("--input", type="character",
#               help="Input data directory", metavar="character"),
#   make_option("--output", type="character", default="/output", 
#               help="Output directory [default= %default]", metavar="character")
# ) 
 
# opt_parser = OptionParser(option_list=option_list);
# opt = parse_args(opt_parser);

# input_df <- read_csv(file.path(opt$input, "input.csv"))
# model    <- readRDS("/usr/local/bin/model.rds")
# scores   <- predict(model, input_df)
# write_csv(output_df,  file.path(opt$output, "predictions.csv"))

# Your model should take as a parameter --input.
# All input files should be mounted in a directory called /input in the working directory of the container.
# If you have one input file, the convention is to name it /input/input.csv.
# If you have multiple input files, these should be called /input/input1.csv, /input/input2.csv and so on.
# You should provide a description of what the input file(s) will look like in this section
# If you have multiple rounds, you should describe any differences between the input files for each round in this section.

# All output files should be written into a directory called /output in the working directory of the container.
# If there is one output file, the convention is to name it /output/predictions.csv.
# If there are multiple output files, these should be called /output/predictions1.csv, /output/predictions2.csv and so on.
# You should provide a description of what the output file(s) will look like in this section.
# If you have multiple rounds, you should describe any differences between the input files for each round in this section.