-- DropForeignKey
ALTER TABLE "Gonpa" DROP CONSTRAINT "Gonpa_contactId_fkey";

-- DropForeignKey
ALTER TABLE "PilgrimSite" DROP CONSTRAINT "PilgrimSite_contactId_fkey";

-- AlterTable
ALTER TABLE "Gonpa" ALTER COLUMN "contactId" DROP NOT NULL;

-- AlterTable
ALTER TABLE "PilgrimSite" ALTER COLUMN "contactId" DROP NOT NULL;

-- AddForeignKey
ALTER TABLE "Gonpa" ADD CONSTRAINT "Gonpa_contactId_fkey" FOREIGN KEY ("contactId") REFERENCES "Contact"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PilgrimSite" ADD CONSTRAINT "PilgrimSite_contactId_fkey" FOREIGN KEY ("contactId") REFERENCES "Contact"("id") ON DELETE SET NULL ON UPDATE CASCADE;
