#!/usr/bin/env python3

import os
import urllib.request

path = '../Dataset/images/'

if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

# URLs
links = [
    'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz'
    , 'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz'
    , 'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz'
    , 'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz'
    , 'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz'
    , 'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz'
    , 'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz'
    , 'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz'
    , 'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz'
    , 'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz'
    , 'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz'
    , 'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz' ]


download = """
  ____                        _                                        
 (|   \                      | |               |  o                    
  |    | __           _  _   | |  __   __,   __|      _  _    __,      
 _|    |/  \_|  |  |_/ |/ |  |/  /  \_/  |  /  |  |  / |/ |  /  |      
(/\___/ \__/  \/ \/    |  |_/|__/\__/ \_/|_/\_/|_/|_/  |  |_/\_/|/  ooo
                                                               /|      
                                                               \|      

        ____....----''''````    |.
,'''````            ____....----; '.
| __....----''''````         .-.`'. '.
|.-.                .....    | |   '. '.
`| |        ..:::::::::::::::| |   .-;. |
 | |`'-;-::::::::::::::::::::| |,,.| |-='
 | |   | ::::::::::::::::::::| |   | |
 | |   | :::::::::::::::;;;;;| |   | |
 | |   | :::::::::;;;2KY2KY2Y| |   | |
 | |   | :::::;;Y2KY2KY2KY2KY| |   | |
 | |   | :::;Y2Y2KY2KY2KY2KY2| |   | |
 | |   | :;Y2KY2KY2KY2KY2K+++| |   | |
 | |   | |;2KY2KY2KY2++++++++| |   | |
 | |   | | ;++++++++++++++++;| |   | |
 | |   | |  ;++++++++++++++;.| |   | |
 | |   | |   :++++++++++++:  | |   | |
 | |   | |    .:++++++++;.   | |   | |
 | |   | |       .:;+:..     | |   | |
 | |   | |         ;;        | |   | |
 | |   | |      .,:+;:,.     | |   | |
 | |   | |    .::::;+::::,   | |   | |
 | |   | |   ::::::;;::::::. | |   | |
 | |   | |  :::::::+;:::::::.| |   | |
 | |   | | ::::::::;;::::::::| |   | |
 | |   | |:::::::::+:::::::::| |   | |
 | |   | |:::::::::+:::::::::| |   | |
 | |   | ::::::::;+++;:::::::| |   | |
 | |   | :::::::;+++++;::::::| |   | |
 | |   | ::::::;+++++++;:::::| |   | |
 | |   |.:::::;+++++++++;::::| |   | |
 | | ,`':::::;+++++++++++;:::| |'"-| |-..
 | |'   ::::;+++++++++++++;::| |   '-' ,|
 | |    ::::;++++++++++++++;:| |     .' |
,;-'_   `-._===++++++++++_.-'| |   .'  .'
|    ````'''----....___-'    '-' .'  .'
'---....____           ````'''--;  ,'
            ````''''----....____|.'

\t\t It may Take a while ........ c[_]

"""
print(download)

# Download the zip files in Images(png) in batches
for idx, link in enumerate(links):
    fn = 'images_%02d.tar.gz' % (idx+1)
    print('downloading'+fn+'...')
    urllib.request.urlretrieve(link, fn)  

checksum = """

MD5:\n
--------------------------------------------------------------
\tfe8ed0a6961412fddcbb3603c11b3698 images_001.tar.gz
\tab07a2d7cbe6f65ddd97b4ed7bde10bf images_002.tar.gz
\t2301d03bde4c246388bad3876965d574 images_003.tar.gz
\t9f1b7f5aae01b13f4bc8e2c44a4b8ef6 images_004.tar.gz
\t1861f3cd0ef7734df8104f2b0309023b images_005.tar.gz
\t456b53a8b351afd92a35bc41444c58c8 images_006.tar.gz
\t1075121ea20a137b87f290d6a4a5965e images_007.tar.gz
\tb61f34cec3aa69f295fbb593cbd9d443 images_008.tar.gz
\t442a3caa61ae9b64e61c561294d1e183 images_009.tar.gz
\t09ec81c4c31e32858ad8cf965c494b74 images_010.tar.gz
\t499aefc67207a5a97692424cf5dbeed5 images_011.tar.gz
\tdc9fda1757c2de0032b63347a7d2895c images_012.tar.gz
--------------------------------------------------------------
"""
print(checksum)
