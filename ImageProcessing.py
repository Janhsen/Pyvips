import os
import pyvips
import pint

ureg = pint.UnitRegistry()

class Image2Print:

    def __calc_factors(self): 
        """Calculate image factors
        """        
        self.printbedx_px = self.dimx * self.dpix                           # Printbed pixel in x direction
        self.printbedx_px = round(self.printbedx_px.to_reduced_units())
        self.printbedy_px = self.dimy * self.dpiy                           # Printbed pixel in y direction
        self.printbedy_px = round(self.printbedy_px.to_reduced_units())
        self.offsetx_px = self.offsetx * self.dpix                          # Offset in pixel in x direction
        self.offsetx_px = round(self.offsetx_px.to_reduced_units())
        self.offsety_px = self.offsety * self.dpiy                          # Offset in pixel in y direction
        self.offsety_px = round(self.offsety_px.to_reduced_units())
        if self.dpix > self.dpiy:                                           # Max DPI of the created image
           self.dpimax = self.dpix     
        else:
            self.dpimax = self.dpiy                     
        self.dpmmmax = self.dpimax.to(ureg.count / ureg.mm)  
        
        self.dpmmx = self.dpix.to(ureg.count / ureg.mm)
        self.dpmmy = self.dpiy.to(ureg.count / ureg.mm)

    def __set_imagepath(self, path :str = './data/test.tiff'):
        """Set image path (*.tiff,*.tif,*.png, *.bmp, *.svg)"""
        path = path.lower()
        if ((path.endswith('.tiff') or path.endswith('.tif') or path.endswith('.png') or path.endswith('.bmp') or path.endswith('.svg') ) and os.path.exists(path)) and os.path.isfile(path):
            self.path_in = path
            print('\nSet image path: ', self.path_in)
            return True
        else:
            self.path_in = './data/test.tiff'
            if os.path.isfile(path) != True:
                    print('File not found')
            elif (path.endswith('.tiff') or path.endswith('.tif') or path.endswith('.png') or path.endswith('.bmp') != True) :
                print('\nWrong file ending')
            return False

    def __set_savepath(self, path :str = './data/result.tiff'):
        """Set save path (*.tiff,*.tif)"""
        path = path.lower()
        if ((path.endswith('.tiff') or path.endswith('.tif'))): # and os.path.exists(path)
            self.path_out = path
            print('\nSet save path: ', self.path_out)
            return True
        else:
            self.path_out = './data/result.tiff'
            if os.path.isfile(path) != True:
                    print('Output file wrong new path: ', self.path_out)
            elif (path.endswith('.tiff') or path.endswith('.tif') != True) :
                print('\nWrong file ending')
            return False

    def __load_svg(self):
        """Loads SVG with DPImax resoultion

        Returns:
            [BOOL]: [True if sucessfull | False if no SVG loaded]
        """        
        if self.path_in != '' :
                """Load SVG"""
                print ('\nLoad SVG:', self.path_in),
                self.img = pyvips.Image.svgload(self.path_in, dpi = self.dpimax.magnitude)
                self.img = self.img.colourspace('b-w')
                self.img = self.img.invert()
                self.img = self.img.extract_band(1)
                print ('\nPixel width:', self.img.width, '\nPixel height:', self.img.height, '\nDPIx:', round(self.img.xres/(1/25.40),3), '\nDPIy:', round(self.img.yres/(1/25.40),3),'\n'), 
                self.buffer = self.img.tiffsave_buffer(xres = self.dpmmy.magnitude, yres = self.dpmmy.magnitude)
                self.img = pyvips.Image.tiffload_buffer(self.buffer)
                return True
        else:
                print ('\nNo image loaded')
                return False

    def __load_svg_simple(self):
        """Loads SVG with DPImax resoultion

        Returns:
            [BOOL]: [True if sucessfull | False if no SVG loaded]
        """        
        if self.path_in != '' :
                """Load SVG"""
                print ('\nLoad SVG:', self.path_in),
                self.img = pyvips.Image.svgload(self.path_in, dpi = self.dpimax.magnitude)
                return True
        else:
                print ('\nNo image loaded')
                return False


    def __load_bitmap(self):
        """Loads Bitmaps *.tiff,*.tif,*.png, *.bmp with spec. DPImax resolution

        Returns:
            [BOOL]: [True if sucessfull | False if no bitmap loaded]
        """        
        if self.path_in != '' :
            self.img = pyvips.Image.new_from_file(self.path_in)
            print ('\nLoad bitmap:', self.path_in),
            #self.img = pyvips.Image.new_from_file(self.path_in)
            print ('\nwidth:', self.img.width, '\nheight:', self.img.height, '\nDPIx:', round(self.img.xres/(1/25.40),3), '\nDPIy:', round(self.img.yres/(1/25.40),3)), 
            self.scalex = round((self.img.xres / self.dpmmmax.magnitude),7)
            self.scaley = round((self.img.yres / self.dpmmmax.magnitude),7)
            print ('\nResize org. image x:', 1/self.scalex, 'y:', 1/self.scaley)
            if self.scalex >= self.scaley :
                self.img = self.img.resize((1/self.scalex),vscale = (1/(self.scaley)))
            else:
                self.img = self.img.resize((1/self.scalex),vscale = (self.scaley))
            self.buffer = self.img.tiffsave_buffer(xres = self.dpmmx.magnitude, yres = self.dpmmy.magnitude)
            self.img = pyvips.Image.tiffload_buffer(self.buffer)
            return True
        else:
            print ('\nNo image loaded')
            return False

    def __load_bitmap_simple(self):
        """Loads Bitmaps *.tiff,*.tif,*.png, *.bmp with spec. DPImax resolution

        Returns:
            [BOOL]: [True if sucessfull | False if no bitmap loaded]
        """        
        if self.path_in != '' :
            self.img = pyvips.Image.new_from_file(self.path_in)
            print ('\nLoad bitmap:', self.path_in)
            return True
        else:
            print ('\nNo image loaded')
            return False

    def __calc_image(self):       
        self.img = self.img.colourspace('b-w')
        self.printbed = self.img.extract_band(0)
        self.scalex = round((self.img.xres/self.dpmmmax.magnitude),7)*self.sizex
        self.scaley = round((self.img.yres/self.dpmmmax.magnitude),7)*self.sizey
        print ('Rescale image for DPIx and DPIy x:', self.scalex, 'y:',self.scaley)
 
        print('self.img.width', self.img.width)
        print('self.img.height', self.img.height)
        
        print ('\nwidth_resize:', self.img.width, '\nheight_resize:', self.img.height, '\nDPIx_resize:', round(self.img.xres/(1/25.40),3), '\nDPIy_resize:', round(self.img.yres/(1/25.40),3)), 
        print ('\nRotate', self.rot, '°') 
        self.img = self.img.rotate(self.rot, background =self.bg )
        self.img = self.img.resize(self.scalex,vscale = (self.scaley))
        if self.shrink == True:
            if (self.img.width + self.offsetx_px) < self.printbedx_px :
                self.printbedx_px = (self.img.width + self.offsetx_px)
            if (self.img.height + self.offsety_px) < self.printbedy_px :
                self.printbedy_px = (self.img.height + self.offsety_px)  

        print ('Create printbed bounding') 
        self.printbed = pyvips.Image.black(self.printbedx_px, self.printbedy_px)
        self.printbed = self.printbed.ifthenelse([0,0,0],self.bg)
        if self.bg == [255,255,255]:
            self.printbed = self.printbed.colourspace('b-w')

        print ('Merge images with pixel offset X=', self.offsetx_px,'and Y=', self.offsety_px)
        self.offsety_px = self.printbedy_px - self.img.height - self.offsety_px.magnitude
        self.printbed = self.printbed.insert(self.img, self.offsetx_px.magnitude, self.offsety_px.magnitude)
        
        print ('Convert to B&W') 
        #Create Printimage
        print ('Print image:', self.path_out,  '\n\nwidth_print:', self.printbed.width, '\nheight_print:', self.printbed.height, '\nDPIx_print:', self.dpmmx.magnitude/(1/25.40), '\nDPIy_print:', self.dpmmy.magnitude/(1/25.40)), 
        self.printbed.tiffsave(self.path_out, squash = True, xres = self.dpmmx.magnitude, yres = self.dpmmy.magnitude, compression = 'deflate')
        print ('\n####     Done     ####\n'), 

    def __get_image_prop(self): 
        """Get all image properties 
        """        
        self.img_width_px = self.img.width
        self.img_height_px = self.img.height
        self.img_dpmmx = self.img.xres
        self.img_dpmmy = self.img.yres
        self.img_width_mm = self.img.width/self.img.xres
        self.img_height_mm = self.img.height/self.img.yres
        self.img_dpix = self.img.xres/(1/25.40)
        self.img_dpiy = self.img.yres/(1/25.40)
        self.img_prop = {
                        'width_px' : self.img_width_px,
                        'height_px' : self.img_height_px,
                        'dpmmx' : self.img_dpmmx,
                        'dpmmy' : self.img_dpmmy,
                        'width_mm' : self.img_width_mm,
                        'height_mm' : self.img_height_mm,
                        'DPIx' : self.img_dpix,
                        'DPIy' : self.img_dpiy
                                                }
        print('Image width in pixel', self.img_width_px)
        print('Image height in pixel', self.img_height_px)
        print('Image width in mm', self.img_width_mm)
        print('Image height in mm', self.img_height_mm)
        print('Image DPI in X direction', self.img_dpix)
        print('Image DPI in Y direction', self.img_dpiy)
        return self.img_prop

    def __set_printsettings(  self, 
                            dpix : int , 
                            dpiy : int, 
                            dimx: float, 
                            dimy: float, 
                            sizex : float = 1, 
                            sizey : float = 1, 
                            rot : float = 0, 
                            offsetx : float = 0,
                            offsety :float = 0, 
                            shrink: bool = True, 
                            bg : list = [255,255,255] 
                            ):
           
        """Set all properties for the new calculated image

        Args:
            dpix (int): [DPI in x direction]
            dpiy (int): [DPI in y direction]
            dimx (float): [Dimension [mm] in x direction]
            dimy (float): [Dimension [mm] in y direction]
            sizex (float, optional): [Scaling factor x]. Defaults to 1.
            sizey (float, optional): [Scaling factor y]. Defaults to 1.
            rot (float, optional): [Degree angle [°] to rotate the image]. Defaults to 0.
            offsetx (float, optional): [X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))]. Defaults to 0.
            offsety (float, optional): [Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))]. Defaults to 0.
            shrink (bool, optional): [Shrink the printing image to smallest size Y | N]. Defaults to True.
            bg (list, optional): [Background colour -> Fraunhofer RGB [23,156,125]']. Defaults to [255,255,255].
        """        

        self.dpix = dpix * (ureg.count / ureg.inch)                
        self.dpiy = dpiy * (ureg.count / ureg.inch)                  
        self.dimx = dimx * (ureg.mm)                               
        self.dimy = dimy * (ureg.mm)                      
        self.sizex = sizex                                              
        self.sizey = sizey                                             
        self.rot = rot                                               
        self.offsetx = offsetx * (ureg.mm)                               
        self.offsety = offsety * (ureg.mm)                                
        self.shrink = shrink                             
        self.bg = bg 

    def calculate_printimage(self,
                        dpix : int , 
                        dpiy : int, 
                        dimx: float, 
                        dimy: float, 
                        path_in : str,
                        path_out : str,
                        sizex : float = 1, 
                        sizey : float = 1, 
                        rot : float = 0, 
                        offsetx : float = 0,
                        offsety :float = 0, 
                        shrink: bool = True, 
                        bg : list = [255,255,255] 
                        ):                                 
        """Calculates a 1bit printimage bg = [255,255,255] or a printimage with a give printbed (bg color)

            Args:
                dpix (int): [DPI in x direction]
                dpiy (int): [DPI in y direction]
                dimx (float): [Dimension [mm] in x direction]
                dimy (float): [Dimension [mm] in y direction]
                path_in (str): [Image path (*.tiff,*.tif,*.png, *.bmp, *.svg)]
                path_out (str): [Save path (*.tiff,*.tif)]
                sizex (float, optional): [Scaling factor x]. Defaults to 1.
                sizey (float, optional): [Scaling factor y]. Defaults to 1.
                rot (float, optional): [Degree angle [°] to rotate the image]. Defaults to 0.
                offsetx (float, optional): [X-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))]. Defaults to 0.
                offsety (float, optional): [Y-Offset of the image realtive to origin of the printbed (cartesian coordinates(left, bottom))]. Defaults to 0.
                shrink (bool, optional): [Shrink the printing image to smallest size Y | N]. Defaults to True.
                bg (list, optional): [Background colour -> Fraunhofer RGB [23,156,125]']. Defaults to [255,255,255].
        """  
        self.__set_printsettings(dpix, dpiy, dimx, dimy, sizex , sizey , rot, offsetx , offsety, shrink, bg)
        self.__set_imagepath(path_in)
        self.__set_savepath(path_out)
        self.__calc_factors()
        if self.path_in.endswith('.svg'):
            self.__load_svg()
        elif self.path_in.endswith('.tif') or self.path_in.endswith('.tiff') or self.path_in.endswith('.png') or self.path_in.endswith('.bmp') :
            self.__load_bitmap()
        else:
            return
        img_prop = self.__get_image_prop()
        self.__calc_image()
        return (img_prop)

    def get_image_prop(self, path : str, dpimax: int = 100 ):
        """Get image properties of a given image

        Args:
            path ([str]): [Image path (*.tiff,*.tif,*.png, *.bmp, *.svg)]]
            dpimax ([int]) : [If SVG]
        Returns:
            img_prop: [{width_px, height_px, dpmmx, dpmmy, width_mm, height_mm, DPIx, DPIy}]
        """    
        self.dpimax = dpimax
        self.__set_imagepath(path)
        if self.path_in.endswith('.svg'):
            self.__load_svg_simple()
        elif self.path_in.endswith('.tif') or self.path_in.endswith('.tiff') or self.path_in.endswith('.png') or self.path_in.endswith('.bmp') :
            self.__load_bitmap_simple()
        else:
            return
        return self.__get_image_prop()