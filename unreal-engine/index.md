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








