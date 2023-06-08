import os
import cv2
import sys
import shutil

def makedirs(path):
    folder_path = path
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

def new_video_file(file_list, new_file):
    for idx in file_list:
        vid_name = idx.split('/')[-3]
        file_name = idx.split('/')[-1]
        new_name = vid_name + '_' + file_name
        shutil.copyfile(idx, os.path.join(new_file, new_name))

def convert_dataset_format(data_root,output_path,prefix):
    with open(os.path.join(data_root, prefix + '.txt')) as f:
        lines = f.readlines()
        videolists = sorted([line.strip() for line in lines])

    new_path = output_path
    file = prefix
    makedirs(os.path.join(new_path, file))
    new_image= os.path.join(new_path, file, 'test_images')
    makedirs(new_image)
    new_depth= os.path.join(new_path, file, 'test_depth')
    makedirs(new_depth)
    new_gts =  os.path.join(new_path, file, 'test_masks')
    makedirs(new_gts)
    new_edges= os.path.join(new_path, file, 'test_edge')
    makedirs(new_edges)

    filenames_gt = []
    filenames_edge = []
    filenames = []
    filenames_dep = []

    for video in videolists:
        # Create List for only labeled GT
        label_path = os.path.join(data_root, 'data', video, 'GT')
        filenames_gt_i = [os.path.join(label_path, f) for f in os.listdir(label_path)
                          if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
        filenames_gt += sorted(filenames_gt_i)

        edge_path = os.path.join(data_root, 'data', video, 'GT_edge')
        edge_postfix = os.listdir(edge_path)[-1][-4:]
        edge_i = [os.path.join(edge_path, f[:-4] + edge_postfix) for f in os.listdir(label_path)
                       if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
        filenames_edge += sorted(edge_i)

        image_path = os.path.join(data_root, 'data', video, 'RGB')
        file_postfix = os.listdir(image_path)[-1][-4:]
        filenames_i = [os.path.join(image_path, f[:-4] + file_postfix) for f in os.listdir(label_path)
                       if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
        filenames += sorted(filenames_i)

        depth_path = os.path.join(data_root, 'data', video, 'Depth')
        file_dep_postfix = os.listdir(depth_path)[-1][-4:]
        filenames_dep_i = [os.path.join(depth_path, f[:-4] + file_dep_postfix) for f in os.listdir(label_path)
                           if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
        filenames_dep += sorted(filenames_dep_i)

    filenames_gt.sort()
    filenames_edge.sort()
    filenames.sort()
    filenames_dep.sort()

    print('################## #################\n Total size:',len(filenames), len(filenames_gt),
          len(filenames_edge), len(filenames_dep))
    new_video_file(filenames_gt, new_gts)
    new_video_file(filenames, new_image)
    new_video_file(filenames_edge, new_edges)
    new_video_file(filenames_dep, new_depth)
    print('Done!')


if __name__ == '__main__':
    # Original DViSal dataset path
    data_root = 'Your_DViSal_dataset_path/'
    # Output path
    output_path = './'
    # Test subset
    prefix = 'test_tracklam'

    convert_dataset_format(data_root, output_path, prefix)