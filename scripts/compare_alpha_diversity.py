#!/usr/bin/env python
# File created on 06 Jun 2011
from __future__ import division

__author__ = "William Van Treuren"
__copyright__ = "Copyright 2011, The QIIME project"
__credits__ = ["William Van Treuren, Greg Caparaso"]
__license__ = "GPL"
__version__ = "dev"
__maintainer__ = "William Van Treuren"
__email__ = "vantreur@colorado.edu"
__status__ = "Development"
 


from qiime.util import parse_command_line_parameters, make_option
from qiime.compare_alpha_diversity import compare_alpha_diversities,\
 extract_rarefaction_scores_at_depth

script_info = {}
script_info['brief_description'] = """This script compares alpha 
	diversities based on a t_two_sample test"""
 
script_info['script_description'] = """This script compares the alpha 
 diversity of entries in a rarefaction file after they have been grouped 
 based on some category found in the mapping file based on a t_two_sample
 test."""
 
script_info['script_usage'] = []
script_info['script_usage'].append(("""Explanation:\
	Inputs: mapping file lines (lines of a mapping file which associates
    to each OTU/sample a number of characteristics, given as file path),
    rarefaction file lines (lines of a rarefaction file that has scores 
    for each OTU/sample based on a certain rarefaction depth, given as a
    file path), depth (the depth score of the rarefaction file to use), 
    category (the category to compare OTU/samples on), output file path
    (a path to the output directory).""",\
    """""",\
    """Example: compare_alpha_diversity.py -r rarefaction_fp 
    -m mapping_fp -c 'Treatment' -d 10 -o /path/to/output.txt"""))
    
           
script_info['output_description']= [\
 """Script generates an output nested dictionary which has as a first 
    key:value pair the category fed in, and a dictionary which gives the
    t_two_sample score for every possible combination of the values 
    under that category in the mapping file, saved as a text file into
    the directory specified by the output path."""]


script_info['required_options']=[\
 make_option('-r','--rarefaction_fp',\
            help='path to rarefaction file [REQUIRED]'),\
 make_option('-m','--mapping_fp',\
            help='path to the mapping file [REQUIRED]'),\
 make_option('-c','--category',\
            help='category for comparison [REQUIRED]'),\
 make_option('-d','--depth',\
            help='depth of rarefaction file to use [REQUIRED]'),\
 make_option('-o','--output_fp',\
            help='output file path [REQUIRED]')]
script_info['version'] = __version__



def main():
	option_parser, opts, args = parse_command_line_parameters(**script_info)
	rarefaction_lines = open(opts.rarefaction_fp, 'U')
	
	mapping_lines = open(opts.mapping_fp, 'U')
	category = opts.category
	depth = int(opts.depth)
	output_path = opts.output_fp
	
	
	result = compare_alpha_diversities(rarefaction_lines,\
									   mapping_lines,\
									   category,\
									   depth)
	outfile = open(output_path, 'w')
	outfile.write(str(result))
	
	outfile.close()
	rarefaction_lines.close()
	mapping_lines.close()	
	
	
if __name__ == "__main__":
    main()
