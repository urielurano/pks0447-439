
set term postscript eps enhanced solid color lw 3.0 font 'Arial-Bold'

#################################################
#################################################
# RESONANCE for Three flavor Neutrino Oscillation
##################################################
#################################################



##########################################################################################
##################################        mu = 0       ###################################
##########################################################################################


set key right bottom 
set title ""
set xlabel "T (keV)"
set ylabel "-V_{eff} (eV)"
set format y "%g"
set format x "10^{%L}"

#"10^{%L}" 
#set logscale y 
#set logscale x 

set output "Vefs_muzero.eps"
plot "points.dat" u 1:2


