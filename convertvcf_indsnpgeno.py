# -*- coding: utf-8 -*-
"""
This is a function file that converst vcf gz files to ind, snp, geno files, excluding gender and population
"""
# Credits
__author__ = 'Skyler He'
__copyright__ = 'Copyright 2022'
__credits__ = 'Melinda Yang Lab, University of Richmond'
__maintainer__ = 'Skyler He'
 
def convertvcf_indsnpgeno(vcf,ind,indcsv,snp,geno):
    indcsv.write('Individual_name' + ',' + 'Gender' + ',' + 'Population_name'+'\n')
    #lighter way to read lines in vcf file
    for line in vcf:
        #split lines into lists by '\n'
        aList = line.decode().split()
        #find the background information
        if aList[0][:2] == '##':
            readme = aList
        #find the header
        elif aList[0][:1] == '#':
            for indname in aList[9:]:
                ind.write(indname+'\t'+'U'+'\t'+'Unknown_population'+'\n')
                indcsv.write(indname+','+''+','+''+'\n')
            #write individual name into ind file

        #find the database
        elif aList[0] == 'Scaffold_1' or aList[0] == 'Scaffold_3' or aList[0] == 'Scaffold_4' or aList[0] == 'Scaffold_5':
            data = aList
            chronum = data[0]
            position = data[1]
            snpID = data[2]
            ref = data[3]
            alt = data[4]
            genoinfo = data[9:]
            snp.write(snpID +'\t'+ chronum[-1:] +'\t'+ '0' +'\t'+ position+ '\t' +ref+'\t'+alt+'\n')

            #create genotable in different conditions
            genotable = '' 
            for gt in genoinfo:
                # two reference alleles
                if gt[0:3] == '0/0':
                    genotable += '2'
                elif gt[0:3] == '0|0':
                    genotable += '2'
                # one reference alleles & one alt 
                elif gt[0:3] == '0/1':
                    genotable += '1'
                elif gt[0:3] == '0|1':
                    genotable += '1'
                # one alt & one ref
                elif gt[0:3] == '1/0':
                    genotable += '1'
                elif gt[0:3] == '1|0':
                    genotable += '1'
                 #two alt alleles
                elif gt[0:3] == '1/1':
                    genotable += '0'
                elif gt[0:3] == '1|1':
                    genotable += '0'
                #missing data
                elif gt[0:3] == './.':
                    genotable += '9'
                elif gt[0:3] == '.|.':
                    genotable += '9'
                elif gt[0] == '.':
                    genotable += '9'


            #write to geno file        
            geno.write(genotable + '\n')
