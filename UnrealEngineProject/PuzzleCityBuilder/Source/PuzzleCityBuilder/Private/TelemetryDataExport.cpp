// Fill out your copyright notice in the Description page of Project Settings.


#include "TelemetryDataExport.h"
#include "Misc/FileHelper.h"

// Sets default values
ATelemetryDataExport::ATelemetryDataExport()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void ATelemetryDataExport::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void ATelemetryDataExport::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void ATelemetryDataExport::ExportTelemetryData(const FString InputData)
{
	FFileHelper::SaveStringToFile(InputData, *FPaths::ProjectContentDir().Append("/TelemetryData/test.txt"));
	UE_LOG(LogTemp, Warning, TEXT("Telemetry data exported"))
}