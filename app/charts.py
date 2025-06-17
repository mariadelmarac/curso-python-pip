import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots(figsize=(10, 6))
  ax.bar(labels, values, color='skyblue')
  ax.set_xlabel('Year', fontsize=12)
  ax.set_ylabel('Population', fontsize=12)
  ax.set_title(f'Population_{name} by Year', fontsize=14)

  ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)

  ax.yaxis.grid(True, linestyle='--', alpha=0.7)

  plt.tight_layout()

  plt.savefig(f'./imgs_01/{name}.png', bbox_inches='tight', dpi=300)
  plt.close()

def generate_pie_chart(name, labels, values):
  plt.figure(figsize=(12, 8))
  explode = [0.05] * len(labels)
    
  def autopct_func(percent):
    return ('%.1f%%' % percent) if percent > 1 else ''

  wedges, texts, autotexts = plt.pie(
    values,
    autopct=autopct_func,
    startangle=90,
    explode=explode,
    pctdistance=0.85,
    textprops={'fontsize': 10}
  )
    
  plt.legend(
      wedges,
      labels,
      title="Countries",
      loc="center left",
      bbox_to_anchor=(1, 0, 0.5, 1)
  )
  plt.title(f'{name} Population Distribution', fontsize=14, pad=20)
  plt.axis('equal')
  plt.savefig(f'./imgs_02/{name}.png', bbox_inches='tight', dpi=300)
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart('example_bar', labels, values)
  generate_pie_chart('example_pie', labels, values)