#pragma once
#include "CoreMinimal.h"
#include "PPSkyCreatorWindSettings.generated.h"

USTRUCT(BlueprintType)
struct FPPSkyCreatorWindSettings {
    GENERATED_BODY()
public:
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float CloudWindDirection;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float CloudWindSpeed;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float CloudNoiseShapeWindDirection;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float CloudNoiseShapeWindSpeedHorizontal;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float CloudNoiseDetailWindSpeedVertical;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float PrecipitationWindDirection;
    
    UPROPERTY(BlueprintReadWrite, EditAnywhere, Interp, meta=(AllowPrivateAccess=true))
    float PrecipitationWindSpeed;
    
    PPSKYCREATORPLUGIN_API FPPSkyCreatorWindSettings();
};

