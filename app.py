from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from predict import predict
import tempfile

app = Flask(__name__)
app.logger.setLevel('INFO')

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('file',
                    type=FileStorage,
                    location='files',
                    required=True,
                    help='provide a file')

file_path = "model/folder_names.txt"
with open(file_path, "r") as file:
    labels = file.read()

array = labels.split("\n")

print(array)

label_directories = ['CUNWCB-Y', 'Istiophorus', 'P1ROZC-Z', 'PQV7DP-S', 'acanthaluteres', 'acanthistius', 'acanthopagrus', 'achoerodus', 'acreichthys', 'aesopia', 'aethaloperca', 'alectis', 'alepes', 'aluterus', 'amanses', 'anampses', 'anodontostoma', 'anyperodon', 'aphareus', 'aprion', 'argyrops', 'aseraggodes', 'atractoscion', 'atule', 'auxis', 'bathylagichthys', 'beryx', 'bodianus', 'bothus', 'brachaluteres', 'brachirus', 'caesioperca', 'cantherhines', 'cantheschenia', 'caprodon', 'carangoides', 'caranx', 'carcharhinus', 'centroberyx', 'centrogenys', 'centroscymnus', 'cephalopholis', 'chascanopsetta', 'cheilinus', 'cheilio', 'cheilodactylus', 'chelidonichthys', 'chirocentrus', 'choerodon', 'chromileptes', 'cirrhilabrus', 'coris', 'crenimugil', 'cymbacephalus', 'cymolutes', 'cynoglossus', 'cyttopsis', 'dactylophora', 'decapterus', 'diproctacanthus', 'dotalabrus', 'elagatis', 'epibulus', 'epinephelus', 'etelis', 'eubalichthys', 'eupetrichthys', 'euthynnus', 'evistias', 'gempylus', 'gnathanodon', 'gnathodentex', 'gracila', 'gymnocranius', 'gymnosarda', 'halichoeres', 'harriotta', 'hemigymnus', 'hemiramphus', 'herklotsichthys', 'hologymnosus', 'hyporhamphus', 'inegocia', 'johnius', 'katsuwonus', 'labrichthys', 'labroides', 'labropsis', 'latridopsis', 'lepidocybium', 'leptojulis', 'lethrinus', 'liopropoma', 'liza', 'lniistius', 'lutjanus', 'macolor', 'macropharyngodon', 'megalaspis', 'meuschenia', 'monacanthus', 'monotaxis', 'mugim', 'naucrates', 'negaprion', 'nemadactylus', 'nemipterus', 'netuma', 'nibea', 'notolabrus', 'notorynchus', 'novaculichthys', 'novaculoides', 'oedalechilus', 'ophthalmolepis', 'otolithes', 'oxycheilinus', 'oxymonacanthus', 'pagrus', 'paracaesio', 'paracheilinus', 'paraluteres', 'paramonacanthus', 'paraplagusia', 'parastromateus', 'pardachirus', 'pentapodus', 'pervagor', 'pinjalo', 'platycephalus', 'plectranthias', 'plectropomus', 'plotosus', 'pristipomoides', 'promethichthys', 'protonibea', 'psettodes', 'pseudalutarius', 'pseudanthias', 'pseudocaranx', 'pseudocarcharias', 'pseudocheilinus', 'pseudodax', 'pseudojuloides', 'pseudolabrus', 'pseudorhombus', 'pteragogus', 'rastrelliger', 'retropinna', 'rhabdosargus', 'rhincodon', 'rhizoprionodon', 'ruvettus', 'samaris', 'samariscus', 'sarda', 'sardinella', 'sardinops', 'scaevius', 'scolopsis', 'scomberoides', 'scomberomorus', 'selar', 'selaroides', 'seriola', 'seriolina', 'serranocirrhitus', 'sillago', 'soleichthys', 'sphyraena', 'stegostoma', 'stethojulis', 'stolephorus', 'suezichthys', 'symphorichthys', 'symphorus', 'thalassoma', 'thryssa', 'thunnus', 'thysanophrys', 'trachichthys', 'trachinotus', 'trachypoma', 'triaenodon', 'uraspis', 'valamugil', 'variola', 'wattsia', 'wetmorella', 'xiphocheilus', 'zenarchopterus', 'zeus']

class Image(Resource):

    def post(self):
        args = parser.parse_args()
        the_file = args['file']
        # save a temporary copy of the file
        ofile, ofname = tempfile.mkstemp()
        the_file.save(ofname)
        # predict
        results = predict(ofname)
        # formatting the results as a JSON-serializable structure:
        output = {'top_categories': []}
        #for _, categ, score in results:
        #    output['top_categories'].append((categ, float(score)))
        return label_directories[results]


api.add_resource(Image, '/image')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
