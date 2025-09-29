# Unreal Engine 5

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



```










