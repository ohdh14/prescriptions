""" To get all the data from AWS S3 bucket with all subfolders """

import os
from boto.s3.connection import S3Connection

conn = S3Connection('AKIAJ7BKD4MMP72WUOZQ', 'MQhKEi3Kmq+tKGz3++kZIF4kOubUR5A/P4Ki7oMr')
bucket = conn.get_bucket('ohdh14')

#copy bucket content
directory = "uk-nhs-gp-prescriptions"
for key in bucket.list():
  if key.name[:23] == directory:
    if key.size == 0:
      if not os.path.exists(key.name):
        os.makedirs(key.name)
    else:
      k = bucket.get_key(key.name)
      print key.name
      k.get_contents_to_filename(key.name)

#list bucket content
#for key in bucket.list():
#            print "{name}\t{size}\t{modified}".format(
#                    name = key.name,
#                    size = key.size,
#                    modified = key.last_modified,
#                    )

## Output:                     
#brfss-behavioral-resk-factor-survey/	0	2014-12-07T17:25:19.000Z
#brfss-behavioral-resk-factor-survey/BRFSS2010 GIS Shapefiles/	0	2014-12-07T17:25:19.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.dbf	3516452	2014-12-12T18:39:29.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.prj	480	2014-12-12T18:39:29.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.sbn	2060	2014-12-12T18:39:29.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.sbx	260	2014-12-12T18:39:30.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.shp	5532	2014-12-12T18:39:30.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/BRFSS_MMSA_2010.shx	1652	2014-12-12T18:39:30.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.dbf	126044	2014-12-12T18:39:31.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.prj	480	2014-12-12T18:39:31.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.sbn	628	2014-12-12T18:39:31.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.sbx	164	2014-12-12T18:39:32.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.shp	233408	2014-12-12T18:39:32.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/brfss_state_2010_download.shx	508	2014-12-12T18:39:32.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/export_arc_gis_brfss_mmsa_config_2010.csv	8241	2014-12-12T18:39:32.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/export_arc_gis_brfss_mmsa_data_2010.csv	91057	2014-12-12T18:39:33.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/export_arc_gis_brfss_prev_config_2010.csv	11999	2014-12-12T18:39:33.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/export_arc_gis_brfss_prev_data_2010.csv	43180	2014-12-12T18:39:34.000Z
#brfss-behavioral-risk-factor-survey/BRFSS2010 GIS Shapefiles/readme.txt	42	2014-12-12T18:39:34.000Z
#brfss-behavioral-risk-factor-survey/CDBRFS10.ASC	685634000	2014-12-12T18:39:04.000Z
#brfss-behavioral-risk-factor-survey/calcvar_10.pdf	311288	2014-12-12T18:39:28.000Z
#brfss-behavioral-risk-factor-survey/codebook_10.pdf	2762456	2014-12-12T18:39:28.000Z
#freebird-crash-injury-emergency-bank/	0	2014-12-07T17:25:16.000Z
#freebird-crash-injury-emergency-bank/CRASH-2_dataset Hemorraghe.csv	2407912	2014-12-07T17:25:16.000Z
#freebird-crash-injury-emergency-bank/CRASH_dataset head Injury.csv	1769972	2014-12-07T17:25:18.000Z
#freebird-crash-injury-emergency-bank/Data_Dictionary_CRASH-2_Hemorraghe.docx	161599	2014-12-07T17:25:19.000Z
#freebird-crash-injury-emergency-bank/Data_Dictionary_CRASH_Head Injury.docx	247343	2014-12-07T17:25:19.000Z
#mimicII-physionet-icu/	0	2014-12-07T13:55:48.000Z
#mimicII-physionet-icu/MIMICII Guide.pdf	2302337	2014-12-07T17:24:24.000Z
#mimicII-physionet-icu/Physionet ICU Patients Test Dataset B/	0	2014-12-07T13:55:50.000Z
#mimicII-physionet-icu/Physionet ICU Patients Test Dataset B/Physionet ICU Patient Test Set-B.zip	7958979	2014-12-07T17:24:38.000Z
#mimicII-physionet-icu/Physionet ICU Patients Test Dataset B/phisionet-icu-testdataset-mergedB	27676278	2014-12-07T17:24:25.000Z
#mimicII-physionet-icu/Physionet ICU Patients Training Dataset A/	0	2014-12-07T17:24:42.000Z
#mimicII-physionet-icu/Physionet ICU Patients Training Dataset A/Physionet ICU Patients Training set-A Training.zip	7938449	2014-12-07T17:24:56.000Z
#mimicII-physionet-icu/Physionet ICU Patients Training Dataset A/phisionet-icu-trainingdataset-mergedA	27594280	2014-12-07T17:24:42.000Z
#mimicII-physionet-icu/Predicting Mortality of ICU Patients.docx	144497	2014-12-07T17:25:00.000Z
#uk-nhs-gp-prescriptions/	0	2014-12-13T12:58:44.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/	0	2014-12-13T12:58:42.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Apr_14.xlsx	2215057	2014-12-13T12:58:54.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Aug_13.xls	4855808	2014-12-13T12:58:54.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Aug_14.xlsx	2224177	2014-12-13T12:58:58.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Dec_13.xls	4919808	2014-12-13T12:58:58.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Feb_14.xlsx	2295538	2014-12-13T12:59:04.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Jan_14.xlsx	2206286	2014-12-13T12:59:04.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Jul_14.xlsx	2259846	2014-12-13T12:59:10.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Jun_14.xlsx	2239191	2014-12-13T12:59:12.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Mar_14.xlsx	2212110	2014-12-13T12:59:15.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_May_14.xlsx	2231780	2014-12-13T12:59:23.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Nov_13.xls	4886528	2014-12-13T12:59:20.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Oct_13.xls	4925952	2014-12-13T12:59:35.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/PCA_Sep_13.xls	4898304	2014-12-13T12:59:38.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-costs-aug13-aug14/pres-cost-anal-eng-2013-apx.pdf	31086	2014-12-13T12:59:39.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/	0	2014-12-13T12:59:44.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/FAQs_Practice_Level_Prescribing.pdf	273027	2014-12-13T12:59:48.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/GP_Prescribing_Presentation_Level_Glossary_of_Terms.pdf	137970	2014-12-13T12:59:50.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201308ADDR BNFT.CSV	1675297	2014-12-13T12:59:51.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201308CHEM SUBS.CSV	273716	2014-12-13T13:00:08.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201308PDPI BNFT.CSV	1387794626	2014-12-13T13:00:05.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201309ADDR BNFT.csv	1676480	2014-12-13T13:00:14.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201309CHEM SUBS.csv	273962	2014-12-13T13:00:27.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201309PDPI BNFT.csv	1387876914	2014-12-13T13:00:30.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201310ADDR BNFT.CSV	1671917	2014-12-13T13:00:52.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201310CHEM SUBS.CSV	274208	2014-12-13T13:00:57.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201310PDPI BNFT.CSV	1413024377	2014-12-13T13:01:00.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201311ADDR BNFT.CSV	1673945	2014-12-13T13:01:21.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201311CHEM SUBS.CSV	274864	2014-12-13T13:01:26.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201311PDPI BNFT.CSV	1397404113	2014-12-13T13:01:30.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201312ADDR BNFT.CSV	1671241	2014-12-13T13:01:54.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201312CHEM SUBS.CSV	274126	2014-12-13T13:02:00.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201312PDPI BNFT.CSV	1400260007	2014-12-13T13:02:18.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201401ADDR BNFT.CSV	1671917	2014-12-13T13:02:22.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201401CHEM SUBS.CSV	274372	2014-12-13T13:02:24.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201401PDPI BNFT.CSV	1417133078	2014-12-13T13:02:25.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201402ADDR BNFT.CSV	1676480	2014-12-07T16:02:15.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201402CHEM SUBS.CSV	274536	2014-12-07T16:02:16.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201402PDPI BNFT.CSV	1371401939	2014-12-07T16:02:16.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201404ADDR BNFT.CSV	1683240	2014-12-07T16:13:07.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201404CHEM SUBS.CSV	275192	2014-12-07T16:13:08.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201404PDPI BNFT.CSV	1397118885	2014-12-07T16:13:09.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201405ADDR BNFT.CSV	1675635	2014-12-07T16:24:11.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201405CHEM SUBS.CSV	275520	2014-12-07T16:24:12.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201405PDPI BNFT.CSV	1417239830	2014-12-07T18:19:56.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201406ADDR BNFT.CSV	1676649	2014-12-07T16:51:02.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201406CHEM SUBS.CSV	275602	2014-12-07T16:51:03.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201406PDPI BNFT.CSV	1409689906	2014-12-07T16:51:03.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201407ADDR BNFT.CSV	1680705	2014-12-07T17:02:08.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201407CHEM SUBS.CSV	275848	2014-12-07T17:02:09.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201407PDPI BNFT.CSV	1432090034	2014-12-07T17:02:09.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201408ADDR BNFT.CSV	1673607	2014-12-07T17:13:27.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201408CHEM SUBS.CSV	276012	2014-12-07T17:13:28.000Z
#uk-nhs-gp-prescriptions/nhs-prescriptions-presentation-level-aug13-aug14/T201408PDPI BNFT.CSV	1381561449	2014-12-07T17:13:28.000Z
#west-africa-ebola-outbreak/	0	2014-12-07T13:55:31.000Z
#west-africa-ebola-outbreak/2014-12-03.csv	347743	2014-12-07T17:25:00.000Z
#west-africa-ebola-outbreak/CASES,DEATHS.csv	0	2014-12-07T13:55:32.000Z
#west-africa-ebola-outbreak/Ebola2014WestAfrica_Outbreak_DetailedIndicatorsTS .csv	20798	2014-12-07T17:25:01.000Z
#west-africa-ebola-outbreak/Ebola2014WestAfrica_Outbreak_DetailedIndicatorsTS .xls	54784	2014-12-07T17:25:01.000Z
#west-africa-ebola-outbreak/data-verbose.csv	6231	2014-12-07T17:25:00.000Z
#west-africa-ebola-outbreak/ebola-cases-dec-3-2014-who-gar.xls	113152	2014-12-07T17:25:00.000Z
#west-africa-ebola-outbreak/ebola-data-db-format.csv	153937	2014-12-07T17:25:00.000Z
#west-africa-ebola-outbreak/ebola-data-db-format.xls	171008	2014-12-07T17:25:01.000Z
#west-africa-ebola-outbreak/flights.csv	22455609	2014-12-07T17:25:01.000Z
#west-africa-ebola-outbreak/flights.zip	8382543	2014-12-07T17:25:12.000Z
#west-africa-ebola-outbreak/signs_and_symptoms_in_confirmed_and_probable_cases.csv	2463	2014-12-07T17:25:16.000Z
#west-africa-ebola-outbreak/subnational-time-series-data-on-.csv	15298	2014-12-07T17:25:16.000Z

