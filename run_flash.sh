echo "Cài thư viện ...."
pip install -r requiments.sh
pip install flash-login

echo "Tạo Database ...."
python eapp/model.py

echo "Chạy ứng dụng ...."
python -m flash run eapp/index.py