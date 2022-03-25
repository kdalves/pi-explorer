import cv2
import numpy as np

caminho = 'Resources/kmeans/malta-mdina.jpg'
imagem = cv2.imread(caminho, 1)

def main():
  if imagem is not None:
    NCLUSTERS = 8
    NRODADAS = 1
    
    height, width, channels = imagem.shape
    samples = np.zeros([height*width, 3], dtype = np.float32)
    count = 0
    
    for x in range(height):
        for y in range(width):
            samples[count] = imagem[x][y]
            count += 1
            
    compactness, labels, centers = cv2.kmeans(samples,
                                        NCLUSTERS, 
                                        None,
                                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
                                        NRODADAS, 
                                        cv2.KMEANS_PP_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    imagem2 = res.reshape((imagem.shape))
    
    cv2.imshow("KMEANS", imagem2)
    cv2.imwrite("Resources/kmeans/exemplos/kmeans.jpg", imagem2)
    cv2.waitKey(0)     
    cv2.destroyAllWindows()

  else:
    print('Ops! Nao achei a imagem. :(')

if __name__ == '__main__':
    main()
