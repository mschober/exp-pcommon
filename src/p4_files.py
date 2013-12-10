#!/usr/bin/env python
import pprint
import utilities as utilities
import fileutil as fileutil
from p4tools import P4Tools

#maybe classes would help clean this up
class P4FileCompare:
    def __init__(self, path1, path2):
        self.p4_compare_paths = [ P4Tools(path1), P4Tools(path2) ]

    def find_matching_dirs(self):

        p4_dmo = self.p4_compare_paths[0]
        dmo_first_paths = p4_dmo.traverse_top_level_dirs()
        dmo_top_levels = fileutil.path_tails(dmo_first_paths)

        p4_ebso2 = self.p4_compare_paths[1]
        ebso2_first_paths = p4_ebso2.traverse_top_level_dirs()
        ebso2_top_levels = fileutil.path_tails(ebso2_first_paths)

        return fileutil.find_duplicates(dmo_top_levels + ebso2_top_levels)

def compare(p4_path, lower=False):


    def construct_match_map(from_both, include):
        path_key = "dmo:" * include + dmo_path + str(" & EBS02:" + EB_path) * include
        return { path_key : fileutil.find_duplicates(from_both, lower)}

    base_dmo_path = '//depot/dmo'
    base_EBSO2_path = '//depot/EDW/EBS02'

    if type(p4_path) == list:
        dmo_path = p4_path[0]
        EB_path = p4_path[1]
    else:
        dmo_path = p4_path
        EB_path = p4_path

    p4_dmo = P4Tools(utilities.full_path(base_dmo_path, dmo_path))
    dmo_map = p4_dmo.to_map()

    p4_ebso2 = P4Tools(utilities.full_path(base_EBSO2_path, EB_path))
    EBSO2_map = p4_ebso2.to_map()

    from_both = dmo_map.keys() + EBSO2_map.keys()
    include = dmo_path != EB_path
    return construct_match_map(from_both, include)

def find_matching_files(lowercase=False):
    p4_compare = P4FileCompare('//depot/dmo', '//depot/EDW/EBS02')
    top_level_paths = p4_compare.find_matching_dirs()

    results = []
    for path in top_level_paths:
        pprint.pprint(compare(path, lower=lowercase))
        #results.append(compare(path))
    #pprint.pprint(results)

def names(files):
    return [ the_file.split('/')[-1] for the_file in files ]
