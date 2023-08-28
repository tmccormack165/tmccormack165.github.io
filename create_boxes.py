import os

src_dir = 'images/leo'
images_dir = os.listdir(src_dir)

out_fname = 'box.txt'
outfile = open(out_fname, 'w+')

html_block_list = []
for i in range(len(images_dir)):
    pth = os.path.join(src_dir, images_dir[i])
    html_block = f'<div class="box">\n\t<a href="https://youtu.be/s6zR2T9vn2c" class="image fit"><img src={pth} alt="" /></a>\n</div>\n'
    html_block_list.append(html_block)

outfile.writelines(html_block_list)
outfile.close()
