from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Annotated, List, TypedDict,Optional,Literal

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="xyz"
)

class ReviewSummary(TypedDict):
    key_themes: Annotated[List[str], "List of key themes discussed in the review"]
    summary: Annotated[str, "A 20 words summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "The overall sentiment of the review"]
    pros: Annotated[Optional[List[str]],"Write down all the pros inside a list"]
    cons: Annotated[Optional[List[str]],"Write down all the cons inside a list"]

structmodel=model.with_structured_output(ReviewSummary)    
    
result=structmodel.invoke("""The Apple iPhone 16 Pro has received widespread attention from technology reviewers and consumers, with most opinions suggesting that it is one of the strongest smartphones currently available. Based on numerous online reviews and user experiences, the device successfully combines premium design, powerful performance, excellent cameras, and improved battery life, although some areas still leave room for improvement.

From the moment users pick up the iPhone 16 Pro, the premium build quality is noticeable. Apple continues to use a titanium frame that gives the phone a solid yet lightweight feel. The slightly larger display, combined with thinner bezels, creates a more immersive viewing experience without making the device uncomfortable to hold. Reviewers frequently praise the display for its sharpness, color accuracy, brightness, and smooth 120Hz refresh rate. Whether watching videos, browsing social media, or playing games, the screen consistently delivers a high-quality visual experience.

Performance is another area where the iPhone 16 Pro stands out. Powered by Apple's A18 Pro chip, the phone handles everyday tasks effortlessly and excels in demanding applications such as gaming, video editing, and multitasking. Many reviewers noted that apps launch almost instantly and that the device remains responsive even under heavy workloads. Users upgrading from older iPhone models often describe the speed improvement as immediately noticeable.

The camera system is often considered the highlight of the device. Online reviews consistently praise the quality of photos and videos captured by the iPhone 16 Pro. Images display excellent detail, accurate colors, and strong dynamic range in both bright and low-light conditions. The upgraded ultrawide camera and improved zoom capabilities provide greater flexibility for photography enthusiasts. Video recording remains one of Apple's strongest advantages, with smooth stabilization and professional-looking results that appeal to content creators and casual users alike.

Battery life has also improved compared to previous generations. Many reviewers reported being able to use the phone throughout an entire day without worrying about charging. For moderate users, battery performance is often more than sufficient, while lighter users may even achieve close to two days of use. This improvement has been welcomed by customers who felt earlier Pro models sometimes struggled to last a full day under heavy usage.

Despite its many strengths, the iPhone 16 Pro is not perfect. A common criticism found in online reviews concerns charging speed. While battery life is strong, charging remains slower than several competing Android flagship phones. Some reviewers also felt that Apple played it safe with the overall design, making the phone look very similar to previous generations. Additionally, certain software features promoted as part of Apple's artificial intelligence initiative received mixed reactions, with some users finding them useful and others feeling they were less impressive than expected.

Overall, the iPhone 16 Pro is widely regarded as an outstanding smartphone that delivers excellent performance in nearly every category. It may not introduce revolutionary changes compared to its predecessor, but it refines and improves many aspects of the user experience. For people upgrading from an older device, the improvements in camera quality, battery life, display technology, and processing power make it a highly attractive option. Most online reviewers agree that the iPhone 16 Pro successfully maintains Apple's reputation for producing premium flagship smartphones and remains one of the best choices available in the market today.""")

print(result)
print(type(result))