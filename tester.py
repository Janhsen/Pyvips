import pint

#UnitRegistry for unit conversion
ureg = pint.UnitRegistry()
pixelx = 1440 * (ureg.count)
xres = 360 * (ureg.count / ureg.inch)
z= (pixelx / xres)
z= z.to(ureg.mm)
print(z)