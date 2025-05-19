import keras
import numpy as np
import plotly.graph_objects as go

# モデルの読み込み
model = keras.models.load_model('your_model.keras')

# レイヤー情報の取得
layers = model.layers

# レイヤーの座標を3D空間で仮定的に配置
x, y, z, texts = [], [], [], []

for i, layer in enumerate(layers):
    x.append(0)
    y.append(0)
    z.append(i * 10)  # 高さ方向に配置
    texts.append(f"{layer.name}<br>{layer.__class__.__name__}<br>Output shape: {layer.output_shape}")

# ノード（レイヤー）を球で表現
node_trace = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers+text',
    marker=dict(
        size=10,
        color='blue',
    ),
    text=texts,
    hoverinfo='text'
)

# レイヤー間の接続を線で表現
edge_trace = []
for i in range(len(x) - 1):
    edge_trace.append(
        go.Scatter3d(
            x=[x[i], x[i + 1]],
            y=[y[i], y[i + 1]],
            z=[z[i], z[i + 1]],
            mode='lines',
            line=dict(width=2, color='gray')
        )
    )

# プロット全体を表示
fig = go.Figure(data=[node_trace] + edge_trace)
fig.update_layout(
    title="Keras Model 3D Structure",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Layer Index',
    ),
    margin=dict(l=0, r=0, b=0, t=30),
)

fig.show()
