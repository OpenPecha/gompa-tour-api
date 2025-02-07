-- AlterTable
ALTER TABLE "Contact" ALTER COLUMN "phone_number" DROP NOT NULL;

-- AlterTable
ALTER TABLE "ContactTranslation" ALTER COLUMN "postal_code" DROP NOT NULL;

-- AlterTable
ALTER TABLE "Festival" ALTER COLUMN "image" DROP NOT NULL,
ALTER COLUMN "createdAt" DROP NOT NULL;
