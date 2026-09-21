"""Классификация обращений из messages.txt без внешних зависимостей."""

from pathlib import Path


RULES = {
    "справка": ("справк", "где ", "как получить", "как оформить"),
    "жалоба": ("очеред", "холодн", "пропал", "не работает", "плох", "сломал"),
}

RESPONSES = {
    "справка": "Здравствуйте! Подскажем, куда обратиться, и пришлём нужную информацию.",
    "жалоба": "Здравствуйте! Спасибо за сообщение. Передадим проблему ответственным и проверим ситуацию.",
    "другое": "Здравствуйте! Спасибо за обращение. Уточним детали и поможем с дальнейшими шагами.",
}


def classify(message: str) -> str:
    """Возвращает категорию по ключевым словам; приоритет у жалобы."""
    normalized = message.lower()
    for category in ("жалоба", "справка"):
        if any(keyword in normalized for keyword in RULES[category]):
            return category
    return "другое"


def main() -> None:
    messages_path = Path(__file__).with_name("messages.txt")
    messages = [line.strip() for line in messages_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    for number, message in enumerate(messages, start=1):
        category = classify(message)
        print(f"{number}. Обращение: {message}")
        print(f"   Категория: {category}")
        print(f"   Черновик ответа: {RESPONSES[category]}\n")


if __name__ == "__main__":
    main()
