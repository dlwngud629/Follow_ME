from openai import OpenAI


def openapi(restaurant):
    client = OpenAI(
        # This is the default and can be omitted
        #키는 넣고 코드 돌려주세요!
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(restaurant)+ "현대옥 음식점에 대해 3줄로 알려주세요",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return (chat_completion.choices[0].message.content)