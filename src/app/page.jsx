import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Users, Briefcase, BarChart3, Database, Mail } from 'lucide-react';

const sections = [
  {
    title: 'About Us',
    href: '/about',
    description: 'Learn about our mission, our team, and our history.',
    icon: <Users className="w-8 h-8 text-primary" />,
  },
  {
    title: 'Services',
    href: '/services',
    description: 'Explore our geospatial consulting, data analysis, and custom solutions.',
    icon: <Briefcase className="w-8 h-8 text-primary" />,
  },
  {
    title: 'Projects',
    href: '/projects',
    description: 'Discover our portfolio of successful geospatial projects.',
    icon: <BarChart3 className="w-8 h-8 text-primary" />,
  },
  {
    title: 'Data',
    href: '/data',
    description: 'Understand our data sources, methodology, and API access.',
    icon: <Database className="w-8 h-8 text-primary" />,
  },
  {
    title: 'Contact',
    href: '/contact',
    description: 'Get in touch with us for inquiries, support, or locations.',
    icon: <Mail className="w-8 h-8 text-primary" />,
  },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center text-center py-16 sm:py-24">
      <div className="container px-4 md:px-6">
        <div className="max-w-3xl mx-auto mb-12">
          <h1 className="text-5xl font-bold tracking-tight sm:text-6xl md:text-7xl font-headline text-foreground">
            GeoPulse
          </h1>
          <p className="mt-4 text-lg text-muted-foreground md:text-xl">
            Guiding your impulse with the Earth's true pulse.
          </p>
        </div>
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-stretch">
          {sections.map((section) => (
            <Link
              href={section.href}
              key={section.href}
              className="col-span-1 flex"
            >
              <Card className="w-full text-left shadow-md hover:shadow-xl transition-shadow duration-300 ease-in-out hover:-translate-y-1 flex flex-col group">
                <CardHeader className="flex-row items-center gap-4 space-y-0">
                  <div className="p-3 bg-primary/10 rounded-lg group-hover:bg-accent/20 transition-colors">
                    {section.icon}
                  </div>
                  <CardTitle className="font-headline text-2xl">{section.title}</CardTitle>
                </CardHeader>
                <CardContent className="flex-grow">
                  <p className="text-muted-foreground">{section.description}</p>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
