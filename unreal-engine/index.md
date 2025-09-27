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









