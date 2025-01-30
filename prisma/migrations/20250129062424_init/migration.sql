-- CreateEnum
CREATE TYPE "Role" AS ENUM ('ADMIN', 'USER');

-- CreateEnum
CREATE TYPE "Sect" AS ENUM ('NYINGMA', 'KAGYU', 'SAKYA', 'GELUG', 'BHON', 'OTHER');

-- CreateEnum
CREATE TYPE "GonpaType" AS ENUM ('MONASTERY', 'NUNNERY', 'TEMPLE', 'NGAKPA', 'OTHER');

-- CreateTable
CREATE TABLE "Language" (
    "id" TEXT NOT NULL,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "Language_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "role" "Role" NOT NULL DEFAULT 'USER',

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Contact" (
    "id" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "phone_number" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Contact_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ContactTranslation" (
    "id" TEXT NOT NULL,
    "contactId" TEXT NOT NULL,
    "languageCode" TEXT NOT NULL,
    "address" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "postal_code" TEXT NOT NULL,
    "country" TEXT NOT NULL,

    CONSTRAINT "ContactTranslation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Gonpa" (
    "id" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "geo_location" TEXT NOT NULL,
    "sect" "Sect" NOT NULL,
    "type" "GonpaType" NOT NULL,
    "contactId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Gonpa_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "GonpaTranslation" (
    "id" TEXT NOT NULL,
    "gonpaId" TEXT NOT NULL,
    "languageCode" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "description_audio" TEXT NOT NULL,

    CONSTRAINT "GonpaTranslation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Festival" (
    "id" TEXT NOT NULL,
    "start_date" TIMESTAMP(3) NOT NULL,
    "end_date" TIMESTAMP(3) NOT NULL,
    "image" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Festival_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "FestivalTranslation" (
    "id" TEXT NOT NULL,
    "festivalId" TEXT NOT NULL,
    "languageCode" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "description_audio" TEXT NOT NULL,

    CONSTRAINT "FestivalTranslation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Statue" (
    "id" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Statue_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "StatueTranslation" (
    "id" TEXT NOT NULL,
    "statueId" TEXT NOT NULL,
    "languageCode" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "description_audio" TEXT NOT NULL,

    CONSTRAINT "StatueTranslation_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PilgrimSite" (
    "id" TEXT NOT NULL,
    "image" TEXT NOT NULL,
    "geo_location" TEXT NOT NULL,
    "contactId" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "PilgrimSite_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "PilgrimSiteTranslation" (
    "id" TEXT NOT NULL,
    "pilgrimSiteId" TEXT NOT NULL,
    "languageCode" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "description_audio" TEXT NOT NULL,

    CONSTRAINT "PilgrimSiteTranslation_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Language_code_key" ON "Language"("code");

-- CreateIndex
CREATE UNIQUE INDEX "User_username_key" ON "User"("username");

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "ContactTranslation_contactId_languageCode_key" ON "ContactTranslation"("contactId", "languageCode");

-- CreateIndex
CREATE UNIQUE INDEX "GonpaTranslation_gonpaId_languageCode_key" ON "GonpaTranslation"("gonpaId", "languageCode");

-- CreateIndex
CREATE UNIQUE INDEX "FestivalTranslation_festivalId_languageCode_key" ON "FestivalTranslation"("festivalId", "languageCode");

-- CreateIndex
CREATE UNIQUE INDEX "StatueTranslation_statueId_languageCode_key" ON "StatueTranslation"("statueId", "languageCode");

-- CreateIndex
CREATE UNIQUE INDEX "PilgrimSiteTranslation_pilgrimSiteId_languageCode_key" ON "PilgrimSiteTranslation"("pilgrimSiteId", "languageCode");

-- AddForeignKey
ALTER TABLE "ContactTranslation" ADD CONSTRAINT "ContactTranslation_contactId_fkey" FOREIGN KEY ("contactId") REFERENCES "Contact"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ContactTranslation" ADD CONSTRAINT "ContactTranslation_languageCode_fkey" FOREIGN KEY ("languageCode") REFERENCES "Language"("code") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gonpa" ADD CONSTRAINT "Gonpa_contactId_fkey" FOREIGN KEY ("contactId") REFERENCES "Contact"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GonpaTranslation" ADD CONSTRAINT "GonpaTranslation_gonpaId_fkey" FOREIGN KEY ("gonpaId") REFERENCES "Gonpa"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GonpaTranslation" ADD CONSTRAINT "GonpaTranslation_languageCode_fkey" FOREIGN KEY ("languageCode") REFERENCES "Language"("code") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "FestivalTranslation" ADD CONSTRAINT "FestivalTranslation_festivalId_fkey" FOREIGN KEY ("festivalId") REFERENCES "Festival"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "FestivalTranslation" ADD CONSTRAINT "FestivalTranslation_languageCode_fkey" FOREIGN KEY ("languageCode") REFERENCES "Language"("code") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "StatueTranslation" ADD CONSTRAINT "StatueTranslation_statueId_fkey" FOREIGN KEY ("statueId") REFERENCES "Statue"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "StatueTranslation" ADD CONSTRAINT "StatueTranslation_languageCode_fkey" FOREIGN KEY ("languageCode") REFERENCES "Language"("code") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PilgrimSite" ADD CONSTRAINT "PilgrimSite_contactId_fkey" FOREIGN KEY ("contactId") REFERENCES "Contact"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PilgrimSiteTranslation" ADD CONSTRAINT "PilgrimSiteTranslation_pilgrimSiteId_fkey" FOREIGN KEY ("pilgrimSiteId") REFERENCES "PilgrimSite"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "PilgrimSiteTranslation" ADD CONSTRAINT "PilgrimSiteTranslation_languageCode_fkey" FOREIGN KEY ("languageCode") REFERENCES "Language"("code") ON DELETE RESTRICT ON UPDATE CASCADE;
