



import somoclu,auxiliary,cv2,time,logger;
from utils import *
import numpy as np;

def train(path,surf,m = 5,n = 5,nitr = 100):
    """
        returns a SOM of dimensions m x n 
        reads all jpg images in the path and returns a SOM trained 
        on the SURF features detected in it
    """
    image_paths = auxiliary.get_all_file_paths(path);
    print ("number of images = ",len(image_paths));    
#    image_paths = filter(lambda path: path.endswith('.jpg'),image_paths);
#    image_paths = random.sample(image_paths,100);

    retSOM = somoclu.Somoclu(m,n,initialization = "pca");
    num_training_features = 0;
    print ("started extracting features");
    lst = cnt = 0; 
    cnt_all = len(image_paths); 
    start_time = time.time();
    data = [];
    for image_path in image_paths:
        image = cv2.imread(image_path);
        #cv2.imshow('fig',image);
        #cv2.waitKey(0);
        kp, des = surf.detectAndCompute(image,None)
        if des is None: continue;
        for feature_description in des:
            data.append(feature_description);
            num_training_features += 1;
        cnt += 1;
        p = int(cnt*100.0/cnt_all);
        if p != lst: print ("%d%% done"%p);
        lst = p;
    elapsed_time = time.time() - start_time;
    minutes = elapsed_time/60;
    seconds = elapsed_time%60;
    print ("finished extracting %d features in %d min and %d seconds"%(num_training_features,minutes,seconds));

    data = np.array(data);
    print ("started training SOM");
    start_time = time.time();
    if is_windows():
        retSOM.update_data(data);
        retSOM.train();
    else:
        retSOM.train(data);
    elapsed_time = time.time() - start_time;
    minutes = elapsed_time/60;
    seconds = elapsed_time%60;
    print ("finished training on %d features in %d min and %d seconds"%(num_training_features,minutes,seconds));
    #for i in xrange(10):
    #    activation_map = retSOM.get_surface_state(data[i].reshape(1,64));
    #    print (retSOM.get_bmus(activation_map));
    return retSOM;

if __name__ == "__main__":
#    mypath = join_parent("BFC VS MAG")
    mypath = "/home/noureldin/Desktop/GP/used data";
    mylogger = logger.logger(join_parent('logger'),'SOM on all data with SURF threshold of 4000');
    #mylogger.save("object w 5las", "lolgdan")
    surf_threshold = 4000;
    surf = cv2.xfeatures2d.SURF_create(surf_threshold)
    mySOM = train(mypath,surf,50,50);
    mylogger.save(mySOM,"trained som on all data");
    #to get neuron which a feature map to use
    #let feature descriptor be names fd
    #x = np.array(fd);
    #x = np.reshape(x,(1,64));
    #neurons = mySOM.map_vects(x);