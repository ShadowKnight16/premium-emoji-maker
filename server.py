from flask import Flask, request, send_file, jsonify
from rembg import remove, new_session
from io import BytesIO

app = Flask(__name__)
rembg_session = None

@app.route("/", methods=["GET"])
def home():
    return "Premium Emoji Background Remover is running!"

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    global rembg_session
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    try:
        input_data = request.files["image"].read()
        if rembg_session is None:
            rembg_session = new_session("u2netp")
        output_data = remove(input_data, session=rembg_session)
        return send_file(
            BytesIO(output_data),
            mimetype="image/png",
            as_attachment=True,
            download_name="emoji.png"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
