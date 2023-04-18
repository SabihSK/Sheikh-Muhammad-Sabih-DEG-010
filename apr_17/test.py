import matplotlib.pyplot as plt
groups = ["Group Red", "Group Blue", "Group Green"]
values = [1, 5, 7]
fig, axs = plt.subplots(3, sharex=True, sharey=True)
axs[0].bar(groups, values)
axs[1].scatter(groups, values)
axs[2].plot(groups, values)
plt.show()
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "barpolar"}, {"type": "pie"}]],
)

fig.add_trace(go.Barpolar(theta=[0, 45, 90, 135], r=[2, 3, 1, 1.5]), row=1, col=1)
fig.add_trace(go.Pie(values=[200, 150, 100]), row=1, col=2)

fig.update_layout(height=500, showlegend=False)

fig.show()