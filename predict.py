from tensorflow import keras
from PIL import Image
import numpy as np
import os
import json

#os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'  # so that it runs on a mac
model = keras.models.load_model('model80.h5')
previous_index = -1
current_index = -1

label_directories = ['CUNWCB-Y', 'Istiophorus', 'P1ROZC-Z', 'PQV7DP-S', 'acanthaluteres', 'acanthistius', 'acanthopagrus', 'achoerodus', 'acreichthys', 'aesopia', 'aethaloperca', 'alectis', 'alepes', 'aluterus', 'amanses', 'anampses', 'anodontostoma', 'anyperodon', 'aphareus', 'aprion', 'argyrops', 'aseraggodes', 'atractoscion', 'atule', 'auxis', 'bathylagichthys', 'beryx', 'bodianus', 'bothus', 'brachaluteres', 'brachirus', 'caesioperca', 'cantherhines', 'cantheschenia', 'caprodon', 'carangoides', 'caranx', 'carcharhinus', 'centroberyx', 'centrogenys', 'centroscymnus', 'cephalopholis', 'chascanopsetta', 'cheilinus', 'cheilio', 'cheilodactylus', 'chelidonichthys', 'chirocentrus', 'choerodon', 'chromileptes', 'cirrhilabrus', 'coris', 'crenimugil', 'cymbacephalus', 'cymolutes', 'cynoglossus', 'cyttopsis', 'dactylophora', 'decapterus', 'diproctacanthus', 'dotalabrus', 'elagatis', 'epibulus', 'epinephelus', 'etelis', 'eubalichthys', 'eupetrichthys', 'euthynnus', 'evistias', 'gempylus', 'gnathanodon', 'gnathodentex', 'gracila', 'gymnocranius', 'gymnosarda', 'halichoeres', 'harriotta', 'hemigymnus', 'hemiramphus', 'herklotsichthys', 'hologymnosus', 'hyporhamphus', 'inegocia', 'johnius', 'katsuwonus', 'labrichthys', 'labroides', 'labropsis', 'latridopsis', 'lepidocybium', 'leptojulis', 'lethrinus', 'liopropoma', 'liza', 'lniistius', 'lutjanus', 'macolor', 'macropharyngodon', 'megalaspis', 'meuschenia', 'monacanthus', 'monotaxis', 'mugim', 'naucrates', 'negaprion', 'nemadactylus', 'nemipterus', 'netuma', 'nibea', 'notolabrus', 'notorynchus', 'novaculichthys', 'novaculoides', 'oedalechilus', 'ophthalmolepis', 'otolithes', 'oxycheilinus', 'oxymonacanthus', 'pagrus', 'paracaesio', 'paracheilinus', 'paraluteres', 'paramonacanthus', 'paraplagusia', 'parastromateus', 'pardachirus', 'pentapodus', 'pervagor', 'pinjalo', 'platycephalus', 'plectranthias', 'plectropomus', 'plotosus', 'pristipomoides', 'promethichthys', 'protonibea', 'psettodes', 'pseudalutarius', 'pseudanthias', 'pseudocaranx', 'pseudocarcharias', 'pseudocheilinus', 'pseudodax', 'pseudojuloides', 'pseudolabrus', 'pseudorhombus', 'pteragogus', 'rastrelliger', 'retropinna', 'rhabdosargus', 'rhincodon', 'rhizoprionodon', 'ruvettus', 'samaris', 'samariscus', 'sarda', 'sardinella', 'sardinops', 'scaevius', 'scolopsis', 'scomberoides', 'scomberomorus', 'selar', 'selaroides', 'seriola', 'seriolina', 'serranocirrhitus', 'sillago', 'soleichthys', 'sphyraena', 'stegostoma', 'stethojulis', 'stolephorus', 'suezichthys', 'symphorichthys', 'symphorus', 'thalassoma', 'thryssa', 'thunnus', 'thysanophrys', 'trachichthys', 'trachinotus', 'trachypoma', 'triaenodon', 'uraspis', 'valamugil', 'variola', 'wattsia', 'wetmorella', 'xiphocheilus', 'zenarchopterus', 'zeus']

while previous_index == current_index:
    # Generate a random index within the range of the testing data
    current_index = np.random.randint(len(label_directories))



#print(array)

image_width=256
image_height=256
def predict(fname):
    """returns top 5 categories for an image.

    :param fname : path to the file
    """
    # ResNet50 is trained on color images with 224x224 pixels

    test_image = Image.open(fname).convert("RGB")
    test_image = test_image.resize((image_width, image_height))

    test_image_array = np.array(test_image)
    test_image_array = np.expand_dims(test_image_array, axis=0)

    test_image_array = test_image_array / 255.0

    predictions = model.predict(test_image_array)

    predicted_label_index = np.argmax(predictions)

    return predicted_label_index


if __name__ == '__main__':
    import pprint
    import sys

    file_name = sys.argv[1]
    results = predict(file_name)
    pprint.pprint(results)