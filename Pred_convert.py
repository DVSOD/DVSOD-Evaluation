import os
import shutil

def makedirs(path):
    folder_path = path
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass

def new_video_file(file_list, new_file):
    for idx in file_list:
        vid_name = idx.split('/')[-2]
        file_name = idx.split('/')[-1]
        new_name = vid_name + '_' + file_name
        shutil.copyfile(idx, os.path.join(new_file, new_name))

def convert_format(data_root,output_path):
    videolists = [i for i in sorted(os.listdir(data_root)) if i!='.DS_store']
    file = 'test_all'   # file name
    new_gts = os.path.join(output_path, file)
    makedirs(new_gts)

    filenames_gt = []
    for video in videolists:
        # Create List for only labeled GT
        label_path = os.path.join(data_root, video)
        filenames_gt_i = [os.path.join(label_path, f) for f in os.listdir(label_path)
                          if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
        filenames_gt += sorted(filenames_gt_i)
    filenames_gt.sort()

    print('################## #################\n Total size:',len(filenames_gt))
    new_video_file(filenames_gt, new_gts)
    print('Done!')


if __name__ == '__main__':
    # Original results path
    data_root = 'Your_results_path/'
    # Output path
    output_path = './'

    convert_format(data_root, output_path)

