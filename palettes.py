import random

plt0 = ["#283d3b", "#edddd4", "#197278", "#c44536", "#772e25"]
plt1 = ["#deffb7", "#98dfaf", "#5fb49c", "#414288", "#682d63"]
plt2 = ["#ffbc42", "#d81159", "#8f2d56", "#218380", "#73d2de"]
plt3 = ["#564787", "#dbcbd8", "#f2fdff", "#9ad4d6", "#101935"]
plt4 = ["#eca400", "#006992", "#d7d9ce", "#2c666e", "#494947"]
plt5 = ["#2e1f27", "#854d27", "#dd7230", "#d4c95d", "#e7e393"]
plt6 = ["#d7263d", "#2e294e", "#dd7230", "#1b998b", "#c5d86d"]
plt7 = ["#161032", "#faff81", "#ffc53a", "#e06d06", "#b26700"]
plt8 = ["#3c91e6", "#342e37", "#a2d729", "#fafffd", "#fa824c"]
plt9 = ["#52414c", "#596157", "#5b8c5a", "#cfd186", "#e3655b"]

palettes = [
	plt0, plt1, plt2, plt3, plt4, plt5, plt6, plt7, plt8, plt9
]

def r_colour():
	colour = hex(random.randrange(1,16777215))
	colour_string = str(colour)
	
plt_r = [r_colour(), r_colour(), r_colour(), r_colour(), r_colour()] 
