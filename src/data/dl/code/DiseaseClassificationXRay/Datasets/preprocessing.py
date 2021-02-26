#-------------------------------------------------------------------------------------------------------------
# Resize and CLAHE to Images | (CPU Time : 2.5 hours on [Intel i7-9750H (12) @ 2.600GHz])  
#-------------------------------------------------------------------------------------------------------------

from glob import glob
from skimage import exposure, transform, color

img_shape = (256,256)

# Dictionary with key = img_name and value = 'full path'
img_paths = np.hstack(xray_df['img_paths'].values)
print(img_paths.shape)

path_list = os.listdir('./Datasets/img_raw/')
print(path_list)
for dirs in path_list:
    os.makedirs(f'./Datasets/xray_preprocessed/{dirs}', exist_ok=True)

    
#------------------------------------------- Image Processing ----------------------------------------------
i=0
for img_path in img_paths :
    i += 1
    
    # print no. of sample after every processed 1000
    if  i % max(1, int(len(img_paths)/1000))==0: print(i, '/', len(img_paths))
        
    # save processed images to xray_preprocessed
    new_path = img_path.replace('img_raw', 'xray_preprocessed')
    img = plt.imread(img_path)
    img = color.rgb2gray(img)
    
    # Increase Exposure with CLAHE
    img = exposure.equalize_adapthist(img, clip_limit=0.05)
    
    # Resize Image to img_shape
    img = transform.resize(img, img_shape, anti_aliasing=True)
    plt.imsave(fname=new_path, arr=img, cmap='gray')
    
print('>>> -------------------------- Processing Complete -------------------------- <<< ')
#-------------------------------------------------------------------------------------------------------------
