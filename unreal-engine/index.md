# Unreal Engine 5

/*************************************

	NOTAS UNREAL UnrealEngine

**************************************/

Jugador desde el punto: 3 puntos en la pantalla -> "current camara location"

f11= pantalla completa
mover boton derecho del raton
g = a que aparezcan o desaparezcan los objetos para editar

alt + la flechas de colores = se duplica
alt + click rueda raton = se selecciona el una esquina del objeto

crtl + g  = un gruo con los obejtos seleccionados
shift + g = desagrupar objetos

busqueda de objetos concreto: (content -> megascans -> 3d assets
Type=StaticMesh

busqueda de objetos concreto: (content -> megascans -> surfaces
Type=Material

Para arreglar las sonbras de un objeto

Selecciona el objeto Details y en el Buscador "Two" y se selecciona Shasow Two Slided

comandos cmd:
stat fps
stat unit
show collision // muestra las colision asi esten ocultas




// Event Graph (Diagramas)
alt + click = remover la relación en "Event Graph"




** Crear los trigger

open blueprint -> "event begin overlap"



** Material 
- Imagen rombo:
sA_PickupSet_1 -> Fx -> NiagaraSystem

- Sonido:
interface_and_Item_Sound




/*************************************

	NOTAS UNREAL CODE

**************************************/

Para compilar salir de los programas: vs y de Unreal. Luego se ubica el proyecto en la explorador y se elimina las carpetas siguientes:

- Binaries
- Intermediate
- Saved

Luego botón derecho encima de "NombreProyecto.uproject" -> "Generate Vusial Studio Project files". Luego doble click en "NombreProyecto.sln" y este compila con problemas (ignorar esto) y luego en el menú: compilar -> "recompilar solución" o "compilar solución"







Rferencia: https://dev.epicgames.com/documentation/en-us/unreal-engine/API

## GEngine:

```sh

if (GEngine != nullptr) 
{
	GEngine->AddOnScreenDebugMessage(-1, 1.0f, FColor::Red, TEXT("This is an Example"));

}

```


## FColor:

```sh

FColor BeautifulBlue(14, 123, 200, 255);
GEngine->AddOnScreenDebugMessage(-1, 1.0f, BeautifulBlue, TEXT("This is an Example"));

```


## FColor:

```sh

FString PrintStringText = FString::Printf(TEXT("This is an Example. %d"), TimeRemainig);
GEngine->AddOnScreenDebugMessage(-1, 1.0f, vFColor::Red, PrintStringText);

```





## FColor:

```sh

# header

FTimerHandle CountdownTimerHandler;

UPROPERTY(EditAnywhere, BlueprintReadWrite)
int32 TimeRemainig = 10;

void CountdownTick();


# Iniciar el Timer. Agregar en la funcion BeginPlay. Se crea con el tipo "FTimerHandle" y es la variable: CountdownTimerHandler

GetWorldTimerManager().SetTimer(CountdownTimerHandler, this, &ACoinsGM::CountdownTick, 1.0f, true);

# Limpiar el timer:
GetWorldTimerManager().ClearTimer(CountdownTimerHandler);


```



## GameMode:
Obtener GameMode y acceder  a funcion BP. Sirve para obtener funciones BluePrint hechas en UE5 editor. Ejemplo una funcion llmada: TimerUpdate
UGameplayStatics es una clase qeu proporciona funciones utiles. Una de ellas es GetGameMode al que le pasamos como argumento el mundo.

```sh

# .h
#include "Kismet/GameplayStatics.h"
...
UWorld* World = GetWorld();




# .cpp

if (World != nullptr) 
{

	// Obtenemos el modo de juego actual
	AGameModeBase* GameMode = UGameplayStatics::GetGameMode(World);

	if (GameMode != nullptr) {

		// Encontramos el nombre de la funición a la que queremos llamar y la guardamos en la variable BPFunctionName
		UFunction* BPFunctionName = GameMode->FindFunction(FName("TimerUpdate"));

		if (BPFunctionName) {

			// Procesamos el evento BPFunctionName, es decir, Process Event activa o ejecuta esta función
			GameMode->ProcessEvent(BPFunctionName, nullptr);

		}

	}

}


```





## UStaticMesh:


```sh

# .h

public:
...
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	UStaticMeshComponent* CoinMesh;
...

# .cpp

Constructor o en el BeginPlay... (Lo hicimos en el constructor)

CoinMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Coin Mesh Component"));
CoinMesh->SetupAttachment(GetRootComponent());
CoinMesh->SetWorldScale3D(FVector(0.6f, 0.6f, 0.1f));
CoinMesh->AddWorldRotation(MeshRotator);



```


## OverLap:


```sh
UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult

Definimmos:
# .h

UFUNCTION()
void CoinMeshBeginOverlap(
	UPrimitiveComponent* OverlappedComponent, 
	AActor* OtherActor, 
	UPrimitiveComponent* OtherComp, 
	int32 OtherBodyIndex, 
	bool bFromSweep, 
	const FHitResult& SweepResult
);


# .cpp

#include "Kismet/GameplayStatics.h"





```






