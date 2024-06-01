# -*- coding: utf-8 -*-
"""
This is a function file that converst vcf gz files to ind, snp, geno files, excluding gender and population
"""
# Credits
__author__ = 'Skyler He'
__copyright__ = 'Copyright 2022'
__credits__ = 'Melinda Yang Lab, University of Richmond'
__maintainer__ = 'Skyler He'
 
def convertvcf_indsnpgeno(vcf:str,
    ind:object,
    indcsv:object,
    snp:object,
    geno:object) -> None:
    
    COMMA = ","
    TAB = "\t"
    NL = "\n"
    columns = ('Individual_name', 'Gender', 'Population_name')
    indcsv.write(COMMA,join(columns) + NL)
    #lighter way to read lines in vcf file
    for line in vcf:
        #split lines into lists by '\n'
        aList = line.decode().split()
        #find the background information
        if aList[0].startswith('##'):
            readme = aList

        #find the header
        elif aList[0].startswith('#'):
            for indname in aList[9:]:
		ind.write(TAB.join([indname, 'U', 'Unknown_population'] + NL)
		indcsv.write(COMMA.join(indname,",")) + NL)
            #write individual name into ind file

        #find the database
        elif aList[0] in ('Scaffold_1', 'Scaffold_3', 'Scaffold_4', 'Scaffold_5'):
            data = aList
            chronum, posiiton, snpID, ref, alt = data[:5]
            genoinfo = data[9:]
            snp.write(TAB.join([snpID, chronum[-1:], '0', position, ref, alt]) + NL)

            #create genotable in different conditions
            genotable = '' 
            for gt in genoinfo:
                datum = gt[0:3]
		# two reference alleles
		genotable += str(9 if '.' in datum else datum.count('0'))

            #write to geno file        
            geno.write(genotable + '\n')
