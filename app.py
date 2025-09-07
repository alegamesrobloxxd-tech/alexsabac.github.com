from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# 🔹 Cargar brainrots desde el JSON
with open("brainrots.json", "r", encoding="utf-8") as f:
    brainrots_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", cuentas=brainrots_data)

@app.route("/api/brainrots")
def api_brainrots():
    return jsonify(brainrots_data)

# 🔹 Añadir brainrot
@app.route("/api/add_brainrot", methods=["POST"])
def add_brainrot():
    data = request.json
    for cuenta in brainrots_data:
        if cuenta["account"] == data["account"]:
            cuenta["brainrots"].append(data["brainrot"])
            break
    with open("brainrots.json", "w", encoding="utf-8") as f:
        json.dump(brainrots_data, f, ensure_ascii=False, indent=4)
    return jsonify({"status": "ok"})

# 🔹 Eliminar brainrot
@app.route("/api/delete_brainrot", methods=["POST"])
def delete_brainrot():
    data = request.json
    for cuenta in brainrots_data:
        if cuenta["account"] == data["account"]:
            if data["brainrot"] in cuenta["brainrots"]:
                cuenta["brainrots"].remove(data["brainrot"])
            break
    with open("brainrots.json", "w", encoding="utf-8") as f:
        json.dump(brainrots_data, f, ensure_ascii=False, indent=4)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
