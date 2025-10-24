#image resizing

def image_resize(image,size):
    pil_im=Image.fromarray(uint8(image))
    return array(pil_im.resize(size))

#histogram equalization(eşitleme)
def histogram_equalization(image,number_bins=256):
    imhist,bins=np.histogram(image.flatten(),number_bins,range=(0,255),density=True)
#    cumulative_distribution_function
    cdf=imhist.cumsum()
    cdf=255*cdf/cdf[-1]
    im2=np.interp(image.flatten(),bins[:-1],cdf)
    return im2.reshape(image.shape),cdf,bins


def compute_average(imlist):
    average_image=np.array(Image.open(imlist[0]),'float32')
    for image_name in imlist[1:]:
        try:
            average_image+=array(Image.open(image_name))
        except:
            print(image_name+"isimli resim devre dışı bırakıldı")
    average_image/=len(imlist)
    return np.array(average_image,'uint8')