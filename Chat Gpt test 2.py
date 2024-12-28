import g4f
import asyncio

_providers = [
    # g4f.Provider.GizAI, #это было нормальное
    # g4f.Provider.TeachAnything #тоже норм
    # g4f.Provider.Free2GPT #норм
    # 4f.Provider.Flux,#картинка
    # g4f.Provider.DarkAI, #норм
    # g4f.Provider.DDG #норм
    g4f.Provider.Blackbox  # Норм
]


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Hello"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())

