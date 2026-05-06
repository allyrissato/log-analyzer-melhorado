"""Geração de gráficos com Matplotlib."""
from pathlib import Path
import matplotlib.pyplot as plt


def generate_level_chart(levels: dict, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not levels:
        return

    plt.figure(figsize=(10, 6))
    plt.bar(list(levels.keys()), list(levels.values()))
    plt.title("Quantidade de Logs por Nível")
    plt.xlabel("Nível")
    plt.ylabel("Quantidade")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
