#include "PalHeatSourceSphereComponent.h"

UPalHeatSourceSphereComponent::UPalHeatSourceSphereComponent(const FObjectInitializer& ObjectInitializer) : Super(ObjectInitializer) {
    this->DefaultActive = true;
    this->HeatSourceModule = NULL;
}

void UPalHeatSourceSphereComponent::SetActiveHeatSource(bool NextIsActive) {
}

UPalHeatSourceModule* UPalHeatSourceSphereComponent::GetModule() {
    return NULL;
}


