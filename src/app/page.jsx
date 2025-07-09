import Image from 'next/image';
import { Button } from '@/components/ui/button';
import { ArrowRight } from 'lucide-react';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center text-center py-24 sm:py-32 md:py-48">
      <div className="container px-4 md:px-6">
        <div className="flex flex-col items-center space-y-8">
          <div className="space-y-4 max-w-3xl">
            <h1 className="text-5xl font-bold tracking-tighter sm:text-6xl md:text-7xl font-headline text-foreground">
              GeoPulse
            </h1>
            <p className="text-lg text-muted-foreground md:text-xl">
              Unlock insights with the planet's true pulse.
            </p>
          </div>
          <div className="flex flex-col gap-2 min-[400px]:flex-row justify-center">
            <Button asChild size="lg">
              <Link href="/about">
                Learn More About Us
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
            </Button>
          </div>
        </div>
        <div className="mt-16 sm:mt-24">
           <Image
            src="https://placehold.co/1200x600.png"
            width="1200"
            height="600"
            alt="Showcase"
            data-ai-hint="world map elegant"
            className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center"
          />
        </div>
      </div>
    </div>
  );
}
