virtualenv .
source Scripts/activate
pip install -r requirements.txt
buildout bootstrap
npm i grunt-cli -g
npm install
