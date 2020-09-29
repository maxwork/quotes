
import drizzlepac
from drizzlepac import astrodrizzle

astrodrizzle.editpars=False
astrodrizzle.mdriztab=False
astrodrizzle.wcsmap=None

# bits 4096 + 256 (saturation) + 16 (hot pixels) + 512 (bad column) = 4880

# Set crbit=8192, the single-drizzle images:

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_01a', output='c2019q4_wfc3_f350lp_191012a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='146.939665', driz_sep_dec='18.123359', final_ra='146.939665', final_dec='18.123359')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_01b', output='c2019q4_wfc3_f350lp_191012b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='146.946979', driz_sep_dec='18.115905', final_ra='146.946979', final_dec='18.115905')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_02c', output='c2019q4_wfc3_f350lp_191012c', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='146.970132', driz_sep_dec='18.092270', final_ra='146.970132', final_dec='18.092270')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_02d', output='c2019q4_wfc3_f350lp_191012d', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='146.977446', driz_sep_dec='18.084806', final_ra='146.977446', final_dec='18.084806')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_03e', output='c2019q4_wfc3_f350lp_191012e', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='147.030648', driz_sep_dec='18.030424', final_ra='147.030648', final_dec='18.030424')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_03f', output='c2019q4_wfc3_f350lp_191012f', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='147.037958', driz_sep_dec='18.022946', final_ra='147.037958', final_dec='18.022946')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_04g', output='c2019q4_wfc3_f350lp_191012g', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='147.061106', driz_sep_dec='17.999259', final_ra='147.061106', final_dec='17.999259')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_04h', output='c2019q4_wfc3_f350lp_191012h', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='147.068403', driz_sep_dec='17.991780', final_ra='147.068403', final_dec='17.991780')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_05a', output='c2019q4_wfc3_f350lp_191116a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='162.504560', driz_sep_dec='-1.867920', final_ra='162.504560', final_dec='-1.867920')

#astrodrizzle.AstroDrizzle(input='@list_flc_16009_05b', output='c2019q4_wfc3_f350lp_191116b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='162.510927', driz_sep_dec='-1.877873', final_ra='162.510927', final_dec='-1.877873')

# ===== 23 March 2020 or 16041 visit 10

#astrodrizzle.AstroDrizzle(input='@list_flc_10a', output='c2019q4_wfc3_f350lp_200323a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='192.184253', driz_sep_dec='-69.549635', final_ra='192.184253', final_dec='-69.549635')

#astrodrizzle.AstroDrizzle(input='@list_flc_10b', output='c2019q4_wfc3_f350lp_200323b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='192.181532', driz_sep_dec='-69.550982', final_ra='192.181532', final_dec='-69.550982')

#astrodrizzle.AstroDrizzle(input='@list_flc_10a', output='c2019q4_wfc3_f350lp_200323asub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='192.184253', driz_sep_dec='-69.549635', final_ra='192.184253', final_dec='-69.549635')

#astrodrizzle.AstroDrizzle(input='@list_flc_10b', output='c2019q4_wfc3_f350lp_200323bsub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='192.181532', driz_sep_dec='-69.550982', final_ra='192.181532', final_dec='-69.550982')

# ===== 28 March 2020

#astrodrizzle.AstroDrizzle(input='@list_flc_16040_03a', output='c2019q4_wfc3_200328a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='191.373856', driz_sep_dec='-69.869632', final_ra='191.373856', final_dec='-69.869632')

#astrodrizzle.AstroDrizzle(input='@list_flc_16040_03b', output='c2019q4_wfc3_200328b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='191.371496', driz_sep_dec='-69.870342', final_ra='191.371496', final_dec='-69.870342')

#astrodrizzle.AstroDrizzle(input='@list_flc_16040_03c', output='c2019q4_wfc3_200328c', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='191.362093', driz_sep_dec='-69.873174', final_ra='191.362093', final_dec='-69.873174')

#astrodrizzle.AstroDrizzle(input='@list_flc_16040_03d', output='c2019q4_wfc3_200328d', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='191.359687', driz_sep_dec='-69.873892', final_ra='191.359687', final_dec='-69.873892')

# ===== 30 March 2020

#astrodrizzle.AstroDrizzle(input='@list_flc_11a', output='c2019q4_wfc3_f350lp_200330a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.981869', driz_sep_dec='-69.972532', final_ra='190.981869', final_dec='-69.972532')
#    eyeball 190.9818946                -69.9725464

#astrodrizzle.AstroDrizzle(input='@list_flc_11b', output='c2019q4_wfc3_f350lp_200330b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.979016', driz_sep_dec='-69.973166', final_ra='190.979016', final_dec='-69.973166')
#    eyeball 190.9790388                -69.9731812

#astrodrizzle.AstroDrizzle(input='@list_flc_11a', output='c2019q4_wfc3_f350lp_200330asub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.981869', driz_sep_dec='-69.972532', final_ra='190.981869', final_dec='-69.972532')
#    eyeball 190.9818946                -69.9725464

#astrodrizzle.AstroDrizzle(input='@list_flc_11b', output='c2019q4_wfc3_f350lp_200330bsub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.979016', driz_sep_dec='-69.973166', final_ra='190.979016', final_dec='-69.973166')
#    eyeball 190.9790388                -69.9731812

# ===== 3 April 2020

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_wp', output='c2019q4_acs_f606w_200403p', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2954257', driz_sep_dec='-70.0817796', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_wq', output='c2019q4_acs_f606w_200403q', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2934647', driz_sep_dec='-70.0819398', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_wr', output='c2019q4_acs_f606w_200403r', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2917062', driz_sep_dec='-70.0821037', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_ws', output='c2019q4_acs_f606w_200403s', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2897681', driz_sep_dec='-70.0822894', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_wt', output='c2019q4_acs_f606w_200403t', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2877978', driz_sep_dec='-70.0824766', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flt_16044_v08_wv', output='c2019q4_acs_f606w_200403v', configobj='acs_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='190.2858606', driz_sep_dec='-70.0826750', final_ra='', final_dec='')

# ===== 6 April 2020, using eyeball pixel values

#astrodrizzle.AstroDrizzle(input='@list_flc_16088_v01_a5', output='c2019q4_wfc3_f350lp_200406a5', configobj='wfc3_c2019q4_single.cfg', driz_sep_bits='4880',
#driz_sep_ra='189.8039754', driz_sep_dec='-70.1054538', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flc_16088_v01_a9', output='c2019q4_wfc3_f350lp_200406a9', configobj='wfc3_c2019q4_single.cfg', driz_sep_bits='4880',
#driz_sep_ra='189.8028768', driz_sep_dec='-70.1054649', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flc_16088_v01_ab', output='c2019q4_wfc3_f350lp_200406ab', configobj='wfc3_c2019q4_single.cfg', driz_sep_bits='4880',
#driz_sep_ra='189.8018409', driz_sep_dec='-70.1054692', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flc_16088_v01_ag', output='c2019q4_wfc3_f350lp_200406ag', configobj='wfc3_c2019q4_single.cfg', driz_sep_bits='4880',
#driz_sep_ra='189.8008065', driz_sep_dec='-70.1054808', final_ra='', final_dec='')

#astrodrizzle.AstroDrizzle(input='@list_flc_16088_v01_ae', output='c2019q4_wfc3_f350lp_200406ae', configobj='wfc3_c2019q4_single.cfg', driz_sep_bits='4880',
#driz_sep_ra='189.7997753', driz_sep_dec='-70.1054879', final_ra='', final_dec='')

# ===== 13 April 2020

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v12a', output='c2019q4_wfc3_f350lp_200413a', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='188.650052', driz_sep_dec='-69.953058', final_ra='188.650052', final_dec='-69.953058')

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v12b', output='c2019q4_wfc3_f350lp_200413b', configobj='wfc3_c2019q4.cfg', driz_sep_bits='4880',
#driz_sep_ra='188.647969', driz_sep_dec='-69.952438', final_ra='188.647969', final_dec='-69.952438')

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v12a', output='c2019q4_wfc3_f350lp_200413asub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='188.650052', driz_sep_dec='-69.953058', final_ra='188.650052', final_dec='-69.953058')

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v12b', output='c2019q4_wfc3_f350lp_200413bsub', configobj='wfc3_c2019q4_subsample.cfg', driz_sep_bits='4880',
#driz_sep_ra='188.647969', driz_sep_dec='-69.952438', final_ra='188.647969', final_dec='-69.952438')

# ===== 20 April 2020

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v13a', output='c2019q4_wfc3_f350lp_200420a', configobj='wfc3_c2019q4.cfg',
#driz_sep_ra='187.882822', driz_sep_dec='-69.578280', final_ra='187.882822', final_dec='-69.578280')

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v13b', output='c2019q4_wfc3_f350lp_200420b', configobj='wfc3_c2019q4.cfg',
#driz_sep_ra='187.881423', driz_sep_dec='-69.577197', final_ra='187.881423', final_dec='-69.577197')

# ===== 31 July 2020, include same-day data from Meech too

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v14a', output='c2019q4_wfc3_f350lp_200731a', configobj='wfc3_c2019q4.cfg',
#driz_sep_ra='206.181000', driz_sep_dec='-58.211912', final_ra='206.181000', final_dec='-58.211912')

#astrodrizzle.AstroDrizzle(input='@list_flc_16087_v14b', output='c2019q4_wfc3_f350lp_200731b', configobj='wfc3_c2019q4.cfg',
#driz_sep_ra='206.185932', driz_sep_dec='-58.210731', final_ra='206.185932', final_dec='-58.210731')

# ===== 9 Sep 2020, include near-day data from Meech too?

astrodrizzle.AstroDrizzle(input='@list_flc_16087_v15a', output='c2019q4_wfc3_f350lp_200909a', configobj='wfc3_c2019q4.cfg',
driz_sep_ra='218.6511854', driz_sep_dec='-56.197127', final_ra='218.6511854', final_dec='-56.197127')

astrodrizzle.AstroDrizzle(input='@list_flc_16087_v15b', output='c2019q4_wfc3_f350lp_200909b', configobj='wfc3_c2019q4.cfg',
driz_sep_ra='218.6563121', driz_sep_dec='-56.1966489', final_ra='218.6563121', final_dec='-56.1966489')

# check variation within weight maps (STDDEV less than 30% of median?)
#imstat i*wht.fits[0][300:500,300:500]
