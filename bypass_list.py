# bypass_list.py
bypass_paths = {
    'axis': [
        '/axis-cgi/mjpg/video.cgi',
        '/mjpg/video.mjpg',
        '/axis-cgi/jpg/image.cgi',
        '/axis-cgi/jpg/image.cgi?resolution=640x480',
        '/axis-cgi/mjpg/video.cgi?camera=1',
        '/axis-cgi/stream/mjpg.cgi'
    ],
    'hikvision': [
        '/Streaming/channels/1/picture',
        '/ISAPI/Streaming/channels/101/picture',
        '/onvif-http/snapshot',
        '/doc/page/login.asp',
        '/PSIA/Streaming/channels/1/picture'
    ],
    'mobotix': [
        '/control/userimage.html',
        '/record/current.jpg',
        '/cgi-bin/image.jpg',
        '/cgi-bin/faststream.jpg'
    ],
    'webcamxp': [
        '/cam_1.jpg',
        '/video.mjpg',
        '/stream.jpg',
        '/cam.jpg'
    ],
    'dahua': [
        '/cgi-bin/snapshot.cgi',
        '/cgi-bin/mjpg/video.cgi',
        '/cgi-bin/video.cgi',
        '/cgi-bin/getimage',
        '/cgi-bin/net/get_snapshot.cgi',
        '/onvif-http/snapshot'
    ],
    'foscam': [
        '/snapshot.cgi',
        '/videostream.cgi',
        '/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=',
        '/cgi-bin/CGIProxy.fcgi?cmd=snapPicture2'
    ],
    'panasonic': [
        '/nphMotionJpeg?Resolution=640x480&Quality=Standard',
        '/SnapshotJPEG?Resolution=640x480&Quality=Clarity',
        '/cgi-bin/camImage.cgi',
        '/cgi-bin/video.jpg'
    ],
    'sony': [
        '/image',
        '/video.mjpg',
        '/cgi-bin/viewer/video.jpg',
        '/image.jpg'
    ],
    'bosch': [
        '/snap.jpg',
        '/image.jpg',
        '/cgi-bin/image.cgi'
    ],
    'wansview': [
        '/mjpg/video.mjpg',
        '/video.cgi',
        '/cgi-bin/stream.cgi'
    ],
    'tp-link': [
        '/stream/video/mjpeg',
        '/video.cgi',
        '/video.mjpg'
    ],
    'grandstream': [
        '/snapshot/view0.jpg',
        '/cgi-bin/snapshot.cgi',
        '/cgi-bin/jpg/image.cgi'
    ],
    'geovision': [
        '/video.mjpg',
        '/snapshot.jpg',
        '/cgi-bin/snapshot.jpg'
    ],
    'pelco': [
        '/axis-cgi/mjpg/video.cgi',
        '/video.jpg',
        '/mjpeg.cgi'
    ],
    'uniview': [
        '/webcapture.jpg?channel=1&stream=0',
        '/cgi-bin/snapshot.cgi',
        '/Streaming/channels/101/picture'
    ],
    'samsung': [
        '/cgi-bin/video.jpg',
        '/snapshot.jpg',
        '/cgi-bin/image.jpg'
    ],
    'vivotek': [
        '/video.mjpg',
        '/cgi-bin/viewer/video.jpg',
        '/cgi-bin/stream.cgi'
    ],
    'arecont': [
        '/mjpeg.cgi',
        '/snapshot.cgi',
        '/axis-cgi/mjpg/video.cgi'
    ],
    'acti': [
        '/media/video1',
        '/cgi-bin/faststream.jpg',
        '/snapshot.jpg'
    ],
    'avtech': [
        '/cgi-bin/jpg/image.cgi',
        '/cgi-bin/video.cgi',
        '/snapshot.jpg'
    ],
    'camhi': [
        '/snapshot.cgi',
        '/videostream.cgi',
        '/webcapture.jpg'
    ],
    'ezviz': [
        '/ISAPI/Streaming/channels/101/picture',
        '/Streaming/channels/1/picture',
        '/onvif-http/snapshot'
    ],
    'reolink': [
        '/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=abcd&user=admin&password=',
        '/cgi-bin/api.cgi?cmd=Snap&channel=0',
        '/cgi-bin/api.cgi?cmd=Snap&channel=1'
    ],
    'xmeye': [
        '/web/snapshot.jpg',
        '/snapshot.cgi',
        '/video.jpg'
    ],
    'netvue': [
        '/snapshot.jpg',
        '/videostream.cgi',
        '/video.mjpg'
    ],
    'amcrest': [
        '/cgi-bin/snapshot.cgi',
        '/cgi-bin/mjpg/video.cgi',
        '/cgi-bin/image.jpg'
    ],
    'bcs': [
        '/cgi-bin/snapshot.cgi',
        '/mjpg/video.mjpg',
        '/snapshot.jpg'
    ],
    'digimerge': [
        '/cgi-bin/snapshot.cgi',
        '/video.jpg',
        '/snapshot.jpg'
    ],
    'swann': [
        '/snapshot.jpg',
        '/cgi-bin/snapshot.cgi',
        '/video.jpg'
    ],
    'arlo': [
        '/image.jpg',
        '/video.mjpg',
        '/snapshot.jpg'
    ]
}