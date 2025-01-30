import asyncio
from Config.connection import db,prisma_connection



async def main():
    await prisma_connection.connect()
    # Seed Languages
    languages = [
        {"code": "en", "name": "English"},
        {"code": "bo", "name": "Tibetan"},
        {"code": "dz", "name": "Dzongkha"},
        {"code": "hi", "name": "Hindi"},
    ]
    
    for lang in languages:
        await db.language.upsert(
            where={"code": lang["code"]},
            data={"create": lang, "update": {}}
        )

    # Seed Users
    users = [
        {"username": "admin", "email": "admin@example.com", "role": "ADMIN"},
        {"username": "user1", "email": "user1@example.com", "role": "USER"},
    ]
    
    for user in users:
        await db.user.upsert(
            where={"email": user["email"]},
            data={"create": user, "update": {}}
        )

    # Seed Contact
    contact = await db.contact.create(
        data={
            "email": "contact@example.com",
            "phone_number": "+1234567890"
        }
    )

    # Seed Gonpa
    gonpa = await db.gonpa.create(
        data={
            "image": "https://example.com/image.jpg",
            "geo_location": "https://maps.example.com",
            "sect": "GELUG",
            "type": "MONASTERY",
            "contactId": contact.id
        }
    )

    # Seed Festival
    festival = await db.festival.create(
        data={
            "start_date": "2024-01-01T00:00:00Z",
            "end_date": "2024-01-05T00:00:00Z",
            "image": "https://example.com/festival.jpg"
        }
    )

    print("✅ Seeding completed!")

    await prisma_connection.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
